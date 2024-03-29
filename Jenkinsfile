#!/usr/bin/env groovy

pipeline {

  agent {
        dockerfile true
    }
  
  parameters {
    string(name: 'NAME', defaultValue: 'MELIH', description: 'Name parameter to pass to the Python script')
  }
  
  triggers {
    // @midnight actually means some time between 12:00 AM and 2:59 AM.
    cron('H/5 * * * *')
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

    // Uncomment this to see verbose output in Jenkins
    VERBOSE = true

    // Disabling buffered console output
    PYTHONUNBUFFERED = 1
  }
  
  options {
    buildDiscarder(logRotator(numToKeepStr: '100'))
    //disableConcurrentBuilds()
    //ansiColor('xterm')
  }
  
  stages {
    stage('Test Cronjob Pipeline') {
      steps {
        sh "python /opt/app/main.py ${params.NAME}"
      }
    }
  }
}
