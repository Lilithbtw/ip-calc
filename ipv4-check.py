import re

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
port = 5000


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calculate():
    net = request.form.get("net")
    result = main(net)
    return render_template('calc.html', net=net, result=result)

def main(ip):

    regex = r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}$"

    if re.match(regex, ip):
        frst_ip = ""
        for n in ip:
            if n == ".":
                break
            frst_ip += n 

        final_ip = '{0:08b}'.format(int(frst_ip))[:4]
        match final_ip:
            case "0000" | "0001" | "0010" | "0011" |"0100" | "0101" | "0110" | "0111":
                return "Your IP is class A with a 255.0.0.0 netmask."
            case "1000" | "1001" | "1010" | "1011":
                return "Your IP is class B with a 255.255.0.0 netmask."
            case "1100" | "1101":
                return "Your IP is class C with a 255.255.255.0 netmask."
            case "1110":
                return "Your IP is class D (Multicast)."
            case "1111":
                return "Your IP is class E (Experimental/Reserved)."
            case _:
                return "Could not determine IP class."
    else:
        return "Your value isn't a valid IP."

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=False)