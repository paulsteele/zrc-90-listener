def label = "zrc-90-listener"

podTemplate(label: label, serviceAccount: 'deployments', containers: [
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
    def myRepo = checkout scm
    def gitCommit = myRepo.GIT_COMMIT
    def gitBranch = myRepo.GIT_BRANCH
    def shortGitCommit = "${gitCommit[0..10]}"
    def previousGitCommit = sh(script: "git rev-parse ${gitCommit}~", returnStdout: true)

    stage('Build') {
      container('docker') {
        sh "docker build . -t registry.paul-steele.com/zrc-90:latest"
      }
    }

    if (gitBranch == "master") {
      stage('Push to Registry') {
        container('docker') {
          withDockerRegistry([credentialsId: 'docker-registry', url: "https://registry.paul-steele.com/"]) {
            sh "docker push registry.paul-steele.com/zrc-90:latest"
          }
        }
      }
    }
  }
}