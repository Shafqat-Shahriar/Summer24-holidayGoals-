var express = require ("express");
var bodyParser=require("body-parser");
  var app = express ();
  app.set("view engine","ejs");
  app.use(express.static("public"))
app.use(bodyParser.urlencoded({extended:true}))
app.get("/",function(req,res)
{
   //res.send("<h1>hey gui</h1>");
   res.render("list")
})
app.post("/",function(req,res)
{
   var i = req.body.n;
   console.log(i);
})


  app.listen(3000,function()
  {
   console.log("listening to port 3000");
  })