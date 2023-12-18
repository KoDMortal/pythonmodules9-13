from flask import Flask,json,Response
app=Flask(__name__)
@app.route("/")
def index():
    return "Test"
def is_prime_number(number):
    dividentList=[]
    if number<=1:
        return False
    else:
        i=2
        while i<=number:
            if number%i==0:
                dividentList.append(i)
            i+=1
        if len(dividentList)>1:
            return False
        else:
            return True
@app.route("/prime_number/<input_number>")
def prime_number(input_number):
    number=int(input_number)
    is_prime=is_prime_number(number)
    response={
        "Number":number,
        "isPrime":is_prime
    }
    json_response=json.dumps(response)
    http_response=Response(response=json_response,status=200,mimetype="application/json")
    return http_response
if __name__=="__main__":
    app.run(debug=True)