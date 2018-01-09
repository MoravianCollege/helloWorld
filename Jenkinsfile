node
{
    stage('Fetch')
    {
        checkout scm
    }
    stage('Environment Setup')
    {
        sh '''
          python3 -m venv beer_env
          . beer_env/bin/activate
          python -m pip install -r requirements.txt
          python -m pip install .
          '''
    }
    stage('Unit Testing')
    {
        sh '''
          . beer_env/bin/activate
          python -m pytest
          '''
    }
    stage('Static Analysis')
    {
        sh 'sonar-scanner -Dsonar.projectKey=helloWorld -Dsonar.sources=. -Dsonar.host.url=http://hyperion.cs.moravian.edu:9000 -Dsonar.login=c15ffad6f2e7384b9a0f4307a9dc313194afe202'
    }
}
