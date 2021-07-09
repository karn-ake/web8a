from flask import Flask, render_template, make_response,request
import datetime

app = Flask(__name__)

def records():
    BASE_DIR = 'F:\\learning_python\\Scripts'
    now = datetime.datetime.now()
    day = now.strftime("%d")
    File_name = 'day'+day+'.log'
    with open(BASE_DIR+'\\'+File_name, "r") as a_file:
        records = []
        for line in a_file:
            if line.split(" ")[2] == "Imported":
                records.append(line)
    return records

def fail_records():
    fail_records = records()
    number_of_fail = 0
    for fail_record in fail_records:
        #print (fail_record.split(";")[2])
        fail = fail_record.split(";")[2]
        #print (fail.split(":")[1])
        if int(fail.split(":")[1]) > 0:
            number_of_fail +=1
    return number_of_fail

@app.route('/')
def home():
    results = ["FIX1A",]
    return render_template('index_logs.html',Data=results)

@app.route('/report')
def report():
    results = records()
    l = len(results)
    results = results[l-10:]
    n = fail_records()
    return render_template('index_logs.html',Data=results,N=n)
#    results.mimetype = "text/plain"
#    return results

@app.route('/sql', methods=['GET','POST'])
def my_form_post():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text1 = request.form['Command']
        text2 = request.form['Value1']
        text3 = request.form.get('select')
        text3 = str(text3)
        processed_text1 = text1.upper()+'  '+text3
        processed_text2 = text1.upper()+' '+text2.upper()+' '+text3
        if text3 == '3':
            return processed_text1
        return processed_text2

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',)