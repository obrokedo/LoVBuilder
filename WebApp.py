from flask import Flask
from flask import send_from_directory
import os
from subprocess import call

application = Flask(__name__)

@application.route("/")
def root():
    exists = os.path.isfile('isbuilding')
    toret = ""
    if exists: 
        toret = "<h1 style='color:blue'>Legacies of Veridocia Official Builder</h1><h2 style='color:blue'>A build is currently in process, please wait a few minutes and reload the page</h2>"
    else:
        # toret = "<h1 style='color:blue'>Legacies of Veridocia Official Builder</h1><form action='/build' method='GET'><button>Start Build</button></form>"
        toret = "<html><h1 style='color:blue'>Legacies of Veridocia Official Builder</h1><button id='sub' onclick='sub()'>Start Build</button><script>function sub (){ document.getElementById('sub').disabled = true; const Http = new XMLHttpRequest(); const url='/build'; Http.open('GET', url); Http.send(); Http.onreadystatechange=(e)=>{ alert('Success')}; setTimeout(function(){ location.reload(); }, 2000); }</script></html>"


    if os.path.isfile('LoV-Demo.exe'):
        f=open("build.date", "r")
        dt = f.read().strip()
        f.close()
        toret = toret + '<p/><h2>Latest Build: ' + dt + '</h2>'
        toret = toret + "<form action='/LoV-Demo.exe' method='GET'><button>Download Build</button></form>"
    if os.path.isfile('Build.log'):
        toret = toret + "<form action='/Build.log' method='GET'><button>Download Log</button></form>"
    return toret
        

@application.route("/build")
def build():
    exists = os.path.isfile('isbuilding')
    if exists:
        return ""
    else:
        call('~/BuildWrapper.sh', shell=True)
        return ""

@application.route("/Build.log")
def dllog():
    response = send_from_directory('/home/ubuntu', 'Build.log', as_attachment=True, attachment_filename='Build.log')
    return response

@application.route("/LoV-Demo.exe")
def download():
    response = send_from_directory('/home/ubuntu', 'LoV-Demo.exe', as_attachment=True, attachment_filename='LoV-Demo.exe')
    return response

if __name__ == "__main__":
        application.run(host='0.0.0.0', port=80)
