# Deploy to Redhat Openshift

Deploying is easy. Just create an app and push this repo.
Absolutely no additional steps are required.

*  Create an app in Python-2.7

```sh
rhc app create <your_app_name> python-2.7
```

*  Add Postgresql cartridge and set the database name environment variable.

```sh
rhc cartridge add postgresql-9.2 -a <your_app_name>
rhc env set POSTGRESQL_DB_NAME=<your_db_name> -a <your_app_name>
```

* Push this repo to openshift server.

* Done
