Array.prototype.forEach2() = function(callback) {
    for (var index  in this) {
        console.log(index)
    }
}

var course = [
    'Javascrip',
    'PHP',
    'React'
];

course.forEach(function(course, index) {
    console.log(course, index)
})