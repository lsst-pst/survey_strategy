## Metric Analysis Framework (MAF) with Docker

# About the latest tag (`oboberg/maf:180525`)
- Tag date format is `yy/mm/dd`
- This tag was built with a `eups distrib install lsst_sims -t sims` on Friday, May 25th, 2018.
- The version of `lsst_sims` is 2.8.0.
- Once in a container running the image `setup sims_maf -t sims` will get you the latest version of MAF.
- The uncompressed image size is 11.9 GB.
- This particular image also has jupyter lab installed, it is started from the container in a way similar to a notebook.
   - `jupyter lab --ip=0.0.0.0 --no-browser`
- This image has a full install of `lsst_sims` and could theoretically be used for any of those packages. Currently it has only been test with MAF.

> Note: the behavior of the latest version of jupyter lab has slightly changed. After issuing the command `jupyter lab --ip=0.0.0.0 --no-browser` inside the container you will be presented with a `url` to copy and paste into your local browser, it will look something similar to this: `http://73174a91b751:8888/?token=sometoken`. You need to replace the string `73174a91b751` with `localhost` when copying the link into your browser. This string will of course be different each time you run the `jupyter lab` command, so replace whatever is between `http://` and `:8888`, whith `localhost`. Also, `sometoken` will be an actual token for the notebook and can be copied as is.

# New features
- A new startup script called `pull_repos.sh` has been added to this image tag that will automatically pull the `sims_maf` GitHub repo to bring the `/home/docmaf/repos` directory up to date. The script also takes care of all of the step to `eups delcare` the package and to run `scons`. It can be used in the following way:
~~~
 docker run -it --name my_container_name \
                  -v ${PWD}:/home/docmaf/maf_local \
                  -p 8888:8888 \
                   oboberg/maf:180306 pull_repos.sh
~~~
- Once in the container you will still need to run `setup sims_maf` if you want to use MAF based off of the repo.

## Starting a MAF container

- This assumes you have already installed Docker on your local machine
- The commands in this section should be run on your local machine's command line.
-  `docker pull oboberg/maf:180525`
     - This command will pull the already built Docker image from the Docker hub.
     - This is a **BIG** image (11.3GB)
     - This image uses Python 3.
-  Change directories using `cd` where you would like to run MAF. This directory will be mounted in the Docker container so that your analysis (e.g jupyter notebooks) will be saved to your local machine.
- Start a new docker container using the following command (this needs to be run as one command):
```
 docker run -it --name my_container_name \
                  -v ${PWD}:/home/docmaf/maf_local \
                  -p 8888:8888 \
                   oboberg/maf:180525
```

- Here is what each of lines in this command do:

   - `docker run -it --name my_container_name` tells docker to start a container in an interactive mode (`-it`) with the name (`--name`) `my_container_name`. You can change the name to whatever you would like.

   - `-v ${PWD}:/home/docmaf/maf_local` will mount the present working directory `PWD` inside the container as `/home/docmaf/maf_local`. While in the container **only** things saved in `/home/docmaf/maf_local` will be saved to your local machine when the container is stopped.

   - `-p 8888:8888` maps port `8888` inside the container to port `8888` on your local machine. This will allow you to run jupyter notebooks in your local browser.

   - `oboberg/maf:180525` tells docker which image to use when running the container.

After you have run this command in a terminal you will be inside the docker container and you will have access to its command line. You should see something like this:

`[docmaf@1781bdbf1d96 ~]`

If you `ls` in this home directory (`/home/docmaf`) you will see the following:


`[docmaf@1781bdbf1d96 ~]$ ls`
`maf_local  repos  stack  startup.sh`

# Setting up MAF  (commands to run inside the docker container)
Once you are running the container you still need to setup the environment to run MAF using the following command:

`[docmaf@e5cde5fc7178 ~]$ setup sims_maf`

> **Note**: When the image is built `sims_maf` is `eups declared ` to be based off of the master branch of the GitHub repo. If you would prefer to use the version of `sims_maf` installed by `eups distrib install`, do `setup sims_maf -t sims`.

# Running MAF in a jupyter notebook

Once you have run the `setup sims_maf` command you are ready to start a notebook.

- First, changes directories into `/home/docmaf/maf_local`

- Now run the following:
`[docmaf@e5cde5fc7178 ~]$ jupyter notebook --ip=0.0.0.0 --no-browser`

- You should now see the regular jupyter notebook message:
```
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=some_token
```

- Copy and paste `http://0.0.0.0:8888/?token=some_token` into your favorite browser and you will be ready to start running notebooks.

> Note: the behavior of the latest version of jupyter lab/notebooks has slightly changed. After issuing the command `jupyter lab --ip=0.0.0.0 --no-browser` inside the container you will be presented with a `url` to copy and paste into your local browser, it will look something similar to this: `http://73174a91b751:8888/?token=sometoken`. You need to replace the string `73174a91b751` with `localhost` when copying the link into your browser. This string will of course be different each time you start run the `jupyter lab` command, so replace whatever is between `http://` and `:8888`, whith local host. Also, `sometoken` will be an actual token for the notebook and can be copied as is.

# Code development with Docker

Using these images it is extremely easy to develop new code on your local machine that is then run inside the Docker containers described above.

For the sake of this description, let's say you have cloned a fork of the `sims_maf` GiHub repository into a directory on your local machine called `my_repos`.

Now, when you run the command to start the container you would want to do the following:

```
 docker run -it --name my_container_name \
                  -v ${PWD}:/home/docmaf/maf_local \
                  -v /Users/my_user_name/my_repos:/home/docmaf/my_repos
                  -p 8888:8888 \
                   oboberg/maf:180525
```

>Note: Replace `/Users/my_user_name/` with the correct path before running this command.

Now, after you have run the command and are in the Docker container you need to `eups declare` where you want the system to find `sims_maf`.

`[docmaf@e5cde5fc7178 ~]$ cd my_repos/sims_maf`
`[docmaf@e5cde5fc7178 ~]$ eups declare sims_maf -t $USER -r .`
`[docmaf@e5cde5fc7178 ~]$ setup sims_maf -t $USER`
`[docmaf@e5cde5fc7178 ~]$ scons`

Your environment in the container is now be set up to run off of code in a repository on your local machine. You can now edit code locally and switch branches, and the changes will be available to the container. When switching branches it is best to runs `scons` again.

See [Mixing Installed Stack with Development Repositories](https://confluence.lsstcorp.org/display/SIM/Catalogs+and+MAF) for more examples of how this is done.

