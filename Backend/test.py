from flask import Flask, request, make_response, jsonify, render_template, url_for, redirect
from pony import orm
from flask_cors import CORS
from pony.orm import *

DB = orm.Database()

app = Flask(__name__)
CORS(app)


class Stvar(DB.Entity):
    stvar = orm.Required(str, unique=True)
    namjena = orm.Required(str)
    cijena = orm.Optional(float)


class Profil(DB.Entity):
    ime = orm.Required(str)
    prezime = orm.Required(str)
    korisnickoIme = orm.Required(str)


class Ribe(DB.Entity):
    vrsta = orm.Required(str)
    voda = orm.Required(str)
    lokacija = orm.Required(StrArray)


class UlovljeneRibe(DB.Entity):
    vrsta = orm.Required(str)
    voda = orm.Required(str)
    lokacija = orm.Required(str)


DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)


def get_stvari():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Stvar)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response": "Success", "data": results_list}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def get_profil():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Profil)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response": "Success", "data": results_list}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def get_ribe():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Ribe)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response": "Success", "data": results_list}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def get_upecane_ribe():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in UlovljeneRibe)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response": "Success", "data": results_list}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def add_stvar(json_request):
    try:
        stvar = json_request["stvar"]
        namjena = json_request["namjena"]
        try:
            cijena = json_request["cijena"]
        except ValueError:
            cijena = None
        with orm.db_session:
            Stvar(stvar=stvar, namjena=namjena, cijena=cijena)
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def add_profil(json_request):
    try:
        ime = json_request["ime"]
        prezime = json_request["prezime"]
        korisnickoIme = json_request["korisnickoIme"]
        with orm.db_session:
            Profil(ime=ime, prezime=prezime, korisnickoIme=korisnickoIme)
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def add_ribe(json_request):
    try:
        vrsta = json_request["vrsta"]
        voda = json_request["voda"]
        lokacija = json_request["lokacija"]
        with orm.db_session:
            Ribe(vrsta=vrsta, voda=voda, lokacija=lokacija)
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


def add_upecane_ribe(json_request):
    try:
        vrsta = json_request["vrsta"]
        voda = json_request["voda"]
        lokacija = json_request["lokacija"]
        with orm.db_session:
            UlovljeneRibe(vrsta=vrsta, voda=voda, lokacija=lokacija)
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}


@app.route("/")
def home():
    response = [{
        "id": 1234,
        "proizvod": "jabuka",
        "cijena": 5,
        "dostava": {
            "kupac": "John Smith",
            "adresa": "Rovinjska 14",
            "grad": "Pula"
        }
    }]
    return make_response(jsonify(response), 200)


@app.route("/stvar/vrati", methods=["GET"])
def vrati_stvar():
    response = get_stvari()
    if response["response"] == "Success":
        return make_response(jsonify(response), 200)
        # return make_response(render_template("vrati.html", data=response["data"]), 200)
    else:
        return make_response(jsonify(response), 400)


@app.route("/profil/vrati", methods=["GET"])
def vrati_profil():
    response = get_profil()
    if response["response"] == "Success":
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 400)


@app.route("/ribe/vrati", methods=["GET"])
def vrati_ribe():
    response = get_ribe()
    if response["response"] == "Success":
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 400)


@app.route("/upecaneribe/vrati", methods=["GET"])
def vrati_upecane_ribe():
    response = get_upecane_ribe()
    if response["response"] == "Success":
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 400)


@app.route("/stvar/dodaj", methods=["POST", "GET"])
def dodaj_stvar():
    if request.method == "POST":
        try:
            json_request = {}
            for key, value in request.json.items():
                if value == "":
                    json_request[key] = None
                else:
                    json_request[key] = value
        except Exception as e:
            response = {"response": str(e)}
            return make_response(jsonify(response), 400)

        response = add_stvar(json_request)

        if response["response"] == "Success":
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 400)
    else:
        return make_response(jsonify(response), 200)


@app.route("/profil/dodaj", methods=["POST", "GET"])
def dodaj_profil():
    if request.method == "POST":
        try:
            json_request = {}
            for key, value in request.json.items():
                if value == "":
                    json_request[key] = None
                else:
                    json_request[key] = value
        except Exception as e:
            response = {"response": str(e)}
            return make_response(jsonify(response), 400)

        response = add_profil(json_request)

        if response["response"] == "Success":
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 400)
    else:
        return make_response(jsonify(response), 200)


@app.route("/ribe/dodaj", methods=["POST", "GET"])
def dodaj_ribe():
    if request.method == "POST":
        try:
            json_request = {}
            for key, value in request.form.items():
                if value == "":
                    json_request[key] = None
                else:
                    json_request[key] = value
        except Exception as e:
            response = {"response": str(e)}
            return make_response(jsonify(response), 400)

        response = add_ribe(json_request)

        if response["response"] == "Success":
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 400)
    else:
        return make_response(jsonify(response), 200)


@app.route("/upecaneribe/dodaj", methods=["POST", "GET"])
def dodaj_upecane_ribe():
    if request.method == "POST":
        try:
            json_request = {}
            for key, value in request.json.items():
                if value == "":
                    json_request[key] = None
                else:
                    json_request[key] = value
        except Exception as e:
            response = {"response": str(e)}
            return make_response(jsonify(response), 400)

        response = add_upecane_ribe(json_request)

        if response["response"] == "Success":
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 400)
    else:
        return make_response(jsonify(response), 200)


if __name__ == "__main__":
    app.run(port=3000)
