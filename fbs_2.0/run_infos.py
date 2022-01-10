# This file is intended to provide some "reference information" in a useful form for python.
# The names of each run in a family (as defined in the families described in the simulation releases)
# are provided in a dictionary; their most-likely most-relevant comparison run is included as well.
# The file also provides some additional dictionaries, which may group together given families that
# touch on very related points; an example is the 'intranight' family, which includes some simulations
# looking at exposure time within a visit as well as whether to add a third visit - all of these relate
# to the survey strategy within a night.
# Each grouping or family only includes runs from a single release, that can use a single comparison run.
# Data / dictionaries containing the family information include:
# family  - comment - nicknames - family_baseline - family_version

# Much of the text in this file is intended to be used in jupyter notebooks and thus is markdown.

import numpy as np
import pandas as pd
from IPython.display import display_markdown
import matplotlib.pyplot as plt

### METRICS FOR SHORT DISPLAY
tablemetrics = ['fOArea fO All visits HealpixSlicer',
                'Effective Area (deg) ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                'Nvisits All props',
                'fONv MedianNvis fO All visits HealpixSlicer',
                'Median NVisits u band HealpixSlicer',
                'Median NVisits g band HealpixSlicer',
                'Median NVisits r band HealpixSlicer',
                'Median NVisits i band HealpixSlicer',
                'Median NVisits z band HealpixSlicer',
                'Median NVisits y band HealpixSlicer', ]
tablenames = ['Area with >825 visits/pointing (fO_Area)',
              'Unextincted area i>25.9',
              'Nvisits total',
              'Median Nvis over top 18k (fO_Nv Med)',
              'Median Nvis u band',
              'Median Nvis g band',
              'Median Nvis r band',
              'Median Nvis i band',
              'Median Nvis z band',
              'Median Nvis y band']


class FamilyInfo():
    """A class to hold some high-level documentation of the available simulation runs.
    (making this a class rather than just a file just makes it a little clearer to use in a notebook).
    """

    def __init__(self, run_json_file, stat_csv_file):
        self.family = pd.read_json(run_json_file, orient='index')
        self.summaries = pd.read_csv(stat_csv_file, index_col=0)

    def list_of_families(self):
        """Print a list of the simulation groups under consideration, as of this time. """
        # The families
        displaystring = ''
        family_list = list(self.family.index.values)
        for k in family_list:
            displaystring+= f"**{k}**, with {len(self.family.loc[k]['run'])} simulations.<br>"
        display_markdown(displaystring, raw=True)
        simlist = np.unique(self.family['run'].explode().values)
        print(f'For {len(simlist)} unique simulations in all.')
        return family_list

    def family_data(self, f, normalized=False):
        """Return all the data for hte family in question
        """
        d = pd.DataFrame(self.summaries.loc[self.family.loc[f]['run']])
        if normalized:
            d = d/self.summaries[tablemetrics].loc[self.family.loc[f]['reference']]
        d['Briefly'] = self.family.loc[f]['brief']
        return d


    def family_info(self, f, normalized=False):
        """Print some summary information about the family and return a high-level set of metrics."""
        d = pd.DataFrame(self.summaries[tablemetrics].loc[self.family.loc[f]['run']])
        if normalized:
            d = d/self.summaries[tablemetrics].loc[self.family.loc[f]['reference']]
        d.columns = tablenames
        d['Briefly'] = self.family.loc[f]['brief']
        display_markdown(self.family.loc[f]['description'], raw=True)
        print(f"Most likely comparison run: {self.family.loc[f]['reference']}")
        return d

    def plot_areaNvis(self, f):
        metrics = tablemetrics[0:4]
        names = tablenames[0:4]
        if isinstance(f, list):
            runs = list(self.family.loc[f]['run'].explode().values)
            refrun = self.family.loc[f]['reference'].explode().values[0]
        else:
            runs = list(self.family.loc[f]['run'])
            refrun = self.family.loc[f]['reference']
        if refrun not in runs:
            runs.insert(0, refrun)
        d = self.summaries[metrics].loc[runs]
        nd = norm_df(d, refrun)
        nd.columns = names
        plot(nd, normed=True, figsize=(10, 6), style=['k-', 'k:', 'r-', 'r:'])
        plt.xlim(0, len(nd)-1)
        xlims = plt.xlim()
        if plt.ylim()[0] < 0.50:
            plt.ylim(bottom=0.50)
        if plt.ylim()[1] > 1.5:
            plt.ylim(top=1.5)
        plt.fill_between(xlims, 1.05, plt.ylim()[1], color='g', alpha=0.1)
        plt.fill_between(xlims, 0.95, plt.ylim()[0], color='r', alpha=0.1)


## Some utility functions to normalize a dataframe or plot it - useful for summar stat comparisons

def norm_df(df, norm_run,
            invert_cols=None, reverse_cols=None, mag_cols=None):
    """
    Normalize values in a DataFrame, based on the values in a given run.
    Can normalize some columns (metric values) differently (invert_cols, reverse_cols, mag_cols)
    if those columns are specified; this lets the final normalized dataframe 'look' the same way
    in a plot (i.e. "up" is better (reverse_cols), they center on 1 (mag_cols), and the magnitude scales
    as expected (invert_cols)).

    Parameters
    ----------
    df : pd.DataFrame
        The data frame containing the metric values to compare
    norm_run: str
        The name of the simulation to normalize to (typically family_baseline)
    invert_cols: list
        Columns (metric values) to convert to 1 / value
    reverse_cols: list
        Columns (metric values) to invert (-1 * value)
    mag_cols: list
        Columns (metrics values) to treat as magnitudes (1 + (difference from norm_run))

    Returns
    -------
    pd.DataFrame
        Normalized data frame
    """
    # Copy the dataframe but drop the columns containing only strings
    out_df = df.copy()
    if reverse_cols is not None:
        out_df[reverse_cols] = -out_df[reverse_cols]
    if invert_cols is not None:
        out_df[invert_cols] = 1 / out_df[invert_cols]
    if mag_cols is not None:
        out_df[mag_cols] = 1 + out_df[mag_cols] - out_df[mag_cols].loc[norm_run]
    else:
        mag_cols = []
    # which columns are strings?
    string_cols = [c for c, t in zip(df.columns, df.dtypes) if t == 'object']
    cols = [c for c in out_df.columns.values if not (c in mag_cols or c in string_cols)]
    out_df[cols] = 1 + (out_df[cols] - out_df[cols].loc[norm_run]) / out_df[cols].loc[norm_run]
    return out_df

def plot(df, normed=True, style=None, figsize=(10, 6), run_nicknames=None):
    """Plot a DataFrame of metric values.

    Parameters
    ---------
    df: pd.DataFrame
        The dataframe of metric values to plot
    normed: bool, opt
        Is the dataframe normalized or not? (default True)
        If true, adds +/- 5% lines to output
    style: list, opt
        Optional list of line color/style values to use for the plotted metric values
    figsize: tuple, opt
        Figure size
    run_nicknames: list, opt
        Replace the run names in the dataframe with these nicknames
    """
    df.plot(figsize=figsize, style=style)
    plt.legend(loc=(1.01, 0))
    if normed:
        plt.axhline(0.95, alpha=0.3, linestyle=':')
        plt.axhline(1.0, alpha=0.3, linestyle='--')
        plt.axhline(1.05, alpha=0.3, linestyle=':')
    if run_nicknames is not None:
        xnames = run_nicknames
    else:
        xnames = df.index.values
    xi = np.arange(len(xnames))
    plt.xticks(xi, xnames, rotation=90, fontsize='large')
    plt.xlim(0, len(xnames)-1)
    plt.grid('k:', alpha=0.3)
    plt.tight_layout()


def fO_cutoff(df, norm_run):
    """Calculate the Y value for a cutoff line where the fO metric fails SRD req.
    This location changes according to the scaling from the baseline for the family.
    """
    srd_fO_cutoff = df['fONv MedianNvis fO All visits HealpixSlicer'].loc[norm_run]
    srd_fO_cutoff = 825 / srd_fO_cutoff
    return srd_fO_cutoff


def special_family_plots(f, families):
    # These add shading over certain X ranges, that corresponds to broad-scale changes in the
    # survey strategy for each of the families included. There are only a few where this is relevant.
    if f == 'footprint':
        # for footprints, let's add shading for similar kinds of footprints
        ylims = plt.ylim()
        plt.fill_between([0, 0.5], ylims[0], ylims[1], alpha=0.1, color='olive')
        plt.fill_between([0.5, 6.5], ylims[0], ylims[1], alpha=0.1, color='mistyrose')
        plt.fill_between([6.5, 9.5], ylims[0], ylims[1], alpha=0.1, color='yellowgreen')
        plt.fill_between([9.5, 18], ylims[0], ylims[1], alpha=0.1, color='darkorange')
    if f == 'rolling':
        ylims = plt.ylim()
        plt.fill_between([0, 0.5], ylims[0], ylims[1], alpha=0.1, color='olive')
        plt.fill_between([0.5, 6.5], ylims[0], ylims[1], alpha=0.1, color='mistyrose')
        plt.fill_between([6.5, 12.5], ylims[0], ylims[1], alpha=0.1, color='darkorange')
        plt.fill_between([12.5, 18.5], ylims[0], ylims[1], alpha=0.1, color='lightgreen')
        plt.fill_between([18.5, 25], ylims[0], ylims[1], alpha=0.1, color='darkgreen')
    if f == 'potential_schedulers':
        ylims = plt.ylim()
        # shade the nexp2 runs
        xnames = families.family[f]
        nexp2 = np.zeros(len(xnames))
        for i, x in enumerate(xnames):
            if 'nexp2' in x:
                nexp2[i] = 1
        shadesx1 = np.where(nexp2 == 1)[0] - 0.5
        shadesx2 = np.where(nexp2 == 1)[0] + 0.5
        for x1, x2 in zip(shadesx1, shadesx2):
            plt.fill_between([x1, x2], ylims[0], ylims[1], alpha=0.1, color='olive')
    return
