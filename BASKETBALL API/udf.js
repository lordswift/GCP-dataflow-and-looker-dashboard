function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.name = values[1];
    obj.country_name = values[2];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }