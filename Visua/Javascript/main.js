// Array.prototype.forEach2 = function(callback){
//     for (var index in this) {
//         if (this.hasOwnProperty(index)){
//             callback(this[index], index, this)
//         }
//     }
// };

// var courses = [
//     'Javascript',
//     'PHP',
//     'React'
// ];

// courses.push('Java');

// courses.forEach2(function(courses, index, array, ){
//     console.log(courses, index, array)
// })


// Array.prototype.filter2 = function(callback) {
//     var output = [];
//     for (var index in this){
//         if (this.hasOwnProperty(index)){
//             var result = callback(this[index], index, this);
//             if (result){
//                 output.push(this[index]);
//             }
//         }
//     }
//     return output;
// };


// var filterCourses = courses.filter2(function(courses, index, array){
//     return courses.coin > 500
// });

// console.log(filterCourses);

// Array.prototype.every2 = function(callback) {
//     for (var index in this) {
//         if (this.hasOwnProperty(index)) {
//            if (!callback(this[index], index, this)) {
//                return false;
//            }
//         }
//     }
//     return true;
// }
// var courses = [
//     {
//         name: 'Javascript',
//         coin: 300,
//         isFinish: true
//     },
//     {
//         name: 'Java',
//         coin: 310,
//         isFinish: true
//     },
//     {
//         name: 'C++',
//         coin: 400,
//         isFinish: true
//     },
//     {
//         name: 'Python',
//         coin: 300,
//         isFinish: true
//     },
//     {
//         name: 'React',
//         coin: 300,
//         isFinish: false
//     }
// ];

// var result = courses.every2(function(courses, index, array){
//     return courses.coin > 100;
// })

// console.log(result);



// var boxElement = document.querySelector('.box');

// boxElement.classList.add('red')

// console.log(boxElement.classList.contains('box', 'red'))


// var aElements = document.querySelectorAll('a')

// for (var i = 0; i < aElements.length; i++) {
//     aElements[i].onclick = function(e) {
//         if (!e.target.href.startsWith('https://f8.edu.vn')) {
//             e.preventDefault();
//         }
//     }
// }

// document.querySelector('div').onclick = function(e) {
//     console.log('DIV');
// }
// document.querySelector('button').onclick = function(e) {
//     e.stopPropagation();
//     console.log('Click me!');
// }
// document.getElementsByClassName





// var json = '["JavaScript", "PHP"]';

// var json2 = '{"name": "Phong Nguyen", "age": 20}'
// var a = 'true';
// console.log(JSON.parse(json2))
var promise = new Promise(
    function(resolve, reject) {
        reject();
    }
)
promise
    .then(function() {
        console.log("Successfully!")
    })
    .catch(function() {
        console.log("Fail!")
    })
    .finally(function() {
        console.log("Done!")
    })