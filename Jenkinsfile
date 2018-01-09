node
{
    stage('Fetch')
    {
        git 'https://github.com/MoravianCollege/helloWorld.git'
    }
    stage('Unit Testing')
    {
        sh 'tox'
    }
    stage('Post Results')
    {
        junit '**/*.xml'
    }
}
