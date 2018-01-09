node
{
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
          pytest
          '''
    }

}
