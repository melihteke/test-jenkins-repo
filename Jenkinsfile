#!/usr/bin/env groovy

pipeline {

  agent {
    // the following will essentially perform a `docker build`, and run all stages (below) in that container.
  dockerfile true
         //dockerfile {
         //additionalBuildArgs '--no-cache'
         //}
  }

  triggers {
    // https://www.jenkins.io/doc/book/pipeline/syntax/#cron-syntax
    // @midnight actually means some time between 12:00 AM and 2:59 AM.
    cron('H 22 15 * *')
    }

  environment {
    
    //NAME = MELIHTEKE
    // Work in production environment
    PROD_ENVIRONMENT = true

    // Set this to true to disable dry run (create devices in DNAC and DNS entries in BlueCat)
    JUST_DO_IT = true

    // Uncomment this to see verbose output in Jenkins
    VERBOSE = true

    // Disabling buffered console output
    PYTHONUNBUFFERED = 1
  }

  options {
    //buildDiscarder(logRotator(numToKeepStr: '100'))
    //disableConcurrentBuilds()
    //ansiColor('xterm')
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
