node
{
    stage('Fetch')
    {
        git 'https://github.com/MoravianCollege/helloWorld.git'
    }
    stage('Unit Testing')
    {
        sh 'pytest'
    }
    stage('Post Results')
    {
        junit '**/*.xml'
    }
}
