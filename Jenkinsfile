node
{
    stage('Fetch')
    {
        checkout scm
    }
    stage('Unit Testing')
    {
        sh 'tox --workdir ~/.env'
    }
    stage('Static Analysis')
    {
        sh 'sonar-scanner -Dsonar.projectKey=helloWorld -Dsonar.host.url=http://hyperion.cs.moravian.edu:9000 -Dsonar.login=c15ffad6f2e7384b9a0f4307a9dc313194afe202'
    }
}
