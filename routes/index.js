var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Home' });
});
router.get('/search', function(req, res, next) {

    console.log(JSON.stringify(req.query));

    var exec = require('child_process').exec;
    var arg1 = req.query['Departure'];
    var arg2 = req.query['Destination'];
    var filename = '../EasyRode/python_utilities/get_Google_info.py'
    exec('python3'+' '+filename+' '+arg1+' '+arg2,function(err,stdout,stderr){
        if(err)
        {
            console.log('stderr',err);
        }
        else if(stdout)
        {
            console.log('stdout',stdout);
            res.render('index', { title: 'Packages', showResult : true , result:JSON.stringify(stdout) });
        }

        else
            res.render('index', { title: 'Packages', showResult : true});
    });



});

module.exports = router;
