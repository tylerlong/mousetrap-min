from fabric.api import local

def update():
    local('rm mousetrap.min.js')
    local('wget https://github.com/ccampbell/mousetrap/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    local('mv mousetrap-master/mousetrap.min.js .')
    local('rm -rf mousetrap-master')
