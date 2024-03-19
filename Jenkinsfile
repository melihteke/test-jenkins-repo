#!/usr/bin/env groovy

pipeline {

  agent {
    docker {
      file 'Dockerfile'
    }
  }

  triggers {
    // @midnight actually means some time between 12:00 AM and 2:59 AM.
    cron('H 22 15 * *')
  }

  environment {
    // Grafana options
    GF_SECURITY_ADMIN_USER = 'admin'
    GF_SECURITY_ADMIN_PASSWORD = 'admin'
    GF_INSTALL_PLUGINS = ''

    // InfluxDB options
    INFLUXDB_DB = 'influx'
    INFLUXDB_ADMIN_USER = 'admin'
    INFLUXDB_ADMIN_PASSWORD = 'admin'

    // Work in production environment
    PROD_ENVIRONMENT = true

    // Set this to true to disable dry run (create devices in DNAC and DNS entries in BlueCat)
    JUST_DO_IT = true

    // Uncomment this to see verbose output in Jenkins
    VERBOSE = true

    // Disabling buffered console output
    PYTHONUNBUFFERED = 1
  }

  stages {
    stage('Test Cronjob Pipeline') {
      when {
        branch 'master'
      }
      steps {
        sh "python /opt/app/main.py"
      }
    }
  }
}
