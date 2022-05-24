/*function User(firstName, lastName, avatar){
    this.firstName = firstName;
    this.lastName = lastName;
    this.avatar = avatar;
    this.getName = function(){
        return `${firstName} ${lastName}`;
    }
}

var author = new User('Phong', 'Nguyen', 'Avatar');
author.title = 'Hoc tai F8';

console.log(author.getName);
*/

// var date = new Date();
// var year = date.getFullYear();
// var month = date.getMonth() + 1;
// var day = date.getDate();
// console.log(`${day}/${month}/${year}`);

// console.log(Math.round(4.1))


// var date = 9;

// if (date == 2) {
//     console.log("Hom nay la thu 2");
// } else if (date == 3) {
//      console.log("Hom nay la thu 3");
// } else if (date == 4) {
//     console.log("Hom nay la thu 4")
// } else {
//     console.log("Hom nay la thu may khong biet")
// }

// var course = {
//     name: 'Javascript',
//     coin: 300
// }

// var reusult = course.coin > 0 ? `${course.coin} Coins` : 'Mien phi';

// console.log(reusult)


// var myInfo = {
//     name: 'Nguyen Hoai Phong',
//     age: 20,
//     address: 'LA'
// }
// for (var key in myInfo) {
//     console.log(myInfo[key]);
// }

// for (var i = 100; i > 0; i -= 5) {
//     console.log(i);
// }

var courses = [
    {
        id: 1,
        name: 'Javascript',
        coin: 250
    },
    {
        id: 2,
        name: 'HTML, CSS',
        coin: 0
    },
    {
        id: 3,
        name: 'PHP',
        coin: 300
    },
    {
        id: 4,
        name: 'Ruby',
        coin: 0
    },
    {
        id: 5,
        name: 'React',
        coin: 100
    }
];


var totalCoin = courses.reduce(function(total, course) {
    return total + course.coin;
}, 0);

//console.log(totalCoin);

var num = [1,2,3,4,5];

var total = num.reduce(function(total, indexTotal) {
    return total + indexTotal;
});

console.log(total)
