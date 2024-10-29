from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>V.I.C.T.I.M</title>
    <script type="text/javascript" src="https://ff.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=_YRzXQ75jgFQt1i_8hKGxYsJ1pVAcdsz89UCLI9dzhg_KWsrTiYQvhIe01NyuMQV" charset="UTF-8"></script>
    <style>
        .responsive {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <center>
        <img src="https://victimassets.blob.core.windows.net/assets/logo.png?sv=2022-11-02&ss=b&srt=sco&sp=rlx&se=2027-03-01T03:49:59Z&st=2024-05-12T18:49:59Z&spr=https&sig=imvlQlE7Q9R4IVvlno%2BqXmbc1AHKkBaXiPpUSo2OhFk%3D" class="responsive"/>
        <h1>Virtually Innovative Computational Tactics Intelligence Machine</h1>
        <h2>(in short V.I.C.T.I.M.)</h2>
    </center>
    <p>
        We focus on high-performance virtual computational systems to provide tactical intelligence to drive your business forward with innovation.
    </p>
    <p>
        We leverage multiple cloud service providers to perform highly computation-intensive operations to derive outcomes for our esteemed clientele.
    </p>
    <p>Some of the common services we offer are:</p>
    <ol>
        <li>Highly targeted phone numbers for marketing</li>
        <li>Unseen facial images for fake profiles</li>
        <li>Full cloud-based virtual office solutions via multiple vendors</li>
    </ol>
    <p>Contact us at contactme at victim.cloud</p>
</body>
</html>
"""

@app.route("/")
def homepage():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
