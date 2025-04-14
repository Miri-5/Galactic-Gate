from flask import Flask, render_template, request , redirect
import voice
#from skyfield.api import load, Topos

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planet/mars')
def mars():
    return render_template('mars.html')
@app.route('/planet/earth')
def earth():
    return render_template('earth.html')
@app.route('/planet/saturn')
def saturn():
    return render_template('saturn.html')
@app.route('/planet/venus')
def venus():
    return render_template('venus.html')
@app.route('/planet/mercury')
def mercury():
    return render_template('mercury.html')
@app.route('/planet/jupiter')
def jupiter():
    return render_template('jupiter.html')
@app.route('/planet/uranus')
def uranus():
    return render_template('uranus.html')
@app.route('/planet/neptune')
def neptune():
    return render_template('neptune.html')
@app.route('/planet/moon')
def moon():
    return render_template('moon.html')
@app.route('/planet/comets')
def comets():
    return render_template('comets.html')
@app.route('/planet/asteroids')
def asteroids():
    return render_template('asteroids.html')
@app.route('/planet/sun')
def sun():
    return render_template('sun.html')
@app.route('/planet/comunication')
def comunication():
    return render_template('comunication.html')


@app.route('/planet_search', methods=['GET', "POST"])
def planet_search():
    query = request.args.get('query')
    if query and query.lower() == 'mercury':
        return redirect('/planet/mercury')
    if query and query.lower() == 'venus':
        return redirect('/planet/venus')
    if query and query.lower() == 'earth':
        return redirect('/planet/earth')
    if query and query.lower() == 'mars':
        return redirect('/planet/mars')
    if query and query.lower() == 'jupiter':
        return redirect('/planet/jupiter')
    if query and query.lower() == 'saturn':
        return redirect('/planet/saturn')
    if query and query.lower() == 'uranus':
        return redirect('/planet/uranus')
    if query and query.lower() == 'neptune':
        return redirect('/planet/neptune')
    if query and query.lower() == 'moon':
        return redirect('/planet/moon')
    if query and query.lower() == 'comets':
        return redirect('/planet/comets')
    if query and query.lower() == 'asteroids':
        return redirect('/planet/asteroids')
    if query and query.lower() == 'sun':
        return redirect('/planet/sun')
    if query and query.lower() == 'comunication':
        return redirect('/planet/comunication')
    return render_template('search_results.html', query=query)

top = ""
sms = ''

@app.route('/record')
def record():
    global sms,top
    sms = top 
    ses = voice.speechen()
    print(ses)
    top = sms + " " + ses
    if ses.lower() == "neptune":
        return redirect('/planet/neptune')
    if ses.lower() == "uranus":
        return redirect('/planet/uranus')
    if ses.lower() == "saturn":
        return redirect('/planet/saturn')
    if ses.lower() == "jupiter":
        return redirect('/planet/jupiter')
    if ses.lower() == "mars":
        return redirect('/planet/mars')
    if ses.lower() == "earth":
        return redirect('/planet/earth')
    if ses.lower() == "venus":
        return redirect('/planet/venus')
    if ses.lower() == "mercury":
        return redirect('/planet/mercury')
    if ses.lower() == "asteroids":
        return redirect('/planet/asteroids')
    if ses.lower() == "comets":
        return redirect('/planet/comets')
    if ses.lower() == "sun":
        return redirect('/planet/sun')
    if ses.lower() == "comunication":
        return redirect('/planet/comunication')    
    
    return render_template('index.html', ses=top)


def index():
    return render_template('index.html')


@app.route("/kayit", methods=["POST"])
def kayit():
    baslik = request.form.get("baslik")
    alt_baslik = request.form.get("alt_baslik")
    metin = request.form.get("metin")
    action = request.form.get("action")

    with open("kayitlar.txt", "a", encoding="utf-8") as f:
        f.write(f"Başlık: {baslik}\n")
        f.write(f"Alt Başlık: {alt_baslik}\n")
        f.write(f"Metin: {metin}\n")
        f.write(f"İşlem: {action}\n")
        f.write("=" * 50 + "\n")

    return "Kaydınız başarıyla alındı! Teşekkürler."
    
'''@app.route('/reckay')
def reckay():
    global sms,top
    sms = top 
    ses = voice.speechtr()
    top = sms + " " + ses
    return render_template('comunication.html', ses=top)
'''

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
