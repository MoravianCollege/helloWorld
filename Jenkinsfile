node
{
    stage('Environment Setup')
    {
        sh '''
          python3 -m venv beer_env
          . beer_env/bin/activate
          pip install -r requirements.txt
          pip install .
          '''
    }
    stage('Unit Testing')
    {
        sh '''
          . beer_env/bin/activate
          pytest
          '''
    }

}
