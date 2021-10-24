from flask import Flask,jsonify,request

app = Flask(__name__)
tasks=[
    {
        "Contact":"8956531595",
        "Name":"XYZ",
        "Done":False,
        "id":1
    },  {
        "Contact":"4548612589",
        "Name":"ABC",
        "Done":False,
        "id":2
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the Contact"
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['id'],
        'Contact':request.json.get('Contact',''),
        'done':False
    }
    tasks.append(contact)
    return jsonify({
            "status":"Success",
            "message":"Contact added successfully"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if __name__=="__main__":
    app.run()
