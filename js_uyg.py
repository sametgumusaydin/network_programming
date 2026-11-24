
############################# get

fetch("https://httpbin.org/get")
  .then(response => response.json())
  .then(data => console.log(data));




############################# post

fetch("https://httpbin.org/post", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        username: "ogrenci",
        course: "Siber Guvenlik"
    })
})
.then(response => response.json())
.then(data => console.log(data));



##########################utf-8 kodlama##########3
const message = "İstanbul Üniversitesi";

const encoder = new TextEncoder();

const encoded = encoder.encode(message);

console.log(encoded);


#######################decode###############

const decoder = new TextDecoder("utf-8");

console.log(decoder.decode(encoded));


################### base64####################

const message = "Siber Guvenlik";

const encoded = btoa(message);

console.log(encoded);

const decoded = atob(encoded);

console.log(decoded);


#######################serialization -deserialization


const student = {
    id: 101,
    name: "Ahmet",
    grade: 85
};

const serialized = JSON.stringify(student);

console.log(serialized);

const deserialized = JSON.parse(serialized);


#########################
Content-Encoding: gzip

################
Content-Encoding: br

console.log(deserialized.name);
