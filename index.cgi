#!/usr/bin/env python
import cgi
from os import environ
import Cookie
import cgitb; cgitb.enable()
parameters = cgi.FieldStorage()
print "Content-type: text/html"
print ""
print """
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="/tc-img/logo-blue-face.png">

        <title>Take Charge</title>

        <!-- Bootstrap core CSS -->
        <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">
"""
if ("home" in parameters.keys()):
    print """
        <!-- Custom styles for this template -->
        <link href="/bootstrap/css/jumbotron-narrow.css" rel="stylesheet">

    """
elif ("leaderboard" in parameters.keys()):
    print """
    <link href="/bootstrap/css/dashboard.css" rel="stylesheet">
    """
else:
    print """
        <!-- Custom styles for this template -->
        <link href="/bootstrap/css/signin.css" rel="stylesheet">
    """
print """
        <link href="/bootstrap/css/style.css" rel="stylesheet">
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>

      <body>

        """

def homePage():
    rating = 0.5
    if (rating < -50):
        color = "red"
    elif (rating > -50 and rating < -15):
        color = "orange"
    elif (rating > -15 and rating < 0):
        color = "#5bc0de"
    else:
        color = "green"
    print """
      <div class="jumbotron" style="margin-top:-20px;background: #fff url('/tc-img/banner1.jpeg') center;height:90vh;background-size:cover;">
      <div style="color:#fff;text-align:left;padding:10px;padding-left:30px;padding-bottom:10vh;margin-top:60vh;width:100%; background-color:#000;">
      <img style="height:100px;"src="/tc-img/logo.png" alt="TakeCharge">
      <p>Make your solar system work for you.</p>
      </div>
      </div>
      <div class="container">
      <div class="jumbotron">
        <div class="row">
        <div class="col-lg-6">
        <h2> Welcome Joe. </h2>
        <div class="circle-black col-lg-offset-2"><span style="color:"""+color+""";"><b>"""+str(rating)+"""</b></span><br/><p class="lead" style="margin-top:-60px;font-size:20px;color:#fff">ChargeScore</p></div>
        <div style="border-bottom:#000 1px solid;"><span style="font-size:16px;"><span style="color:#2C75FF;">generation<span style="font-size:40px;">8</span>
        </span>vs<span style="color:#FBAA1D;">
        <span style="font-size:32px;"><b>7.5</b></span> consumption
        </span>
        </span>
        </div>
        </div>
        <div class="sidemain col-lg-offset-1 col-lg-5">
        <ul class="nav nav-pills nav-stacked">
          <li role="presentation"><a href="?leaderboard=true"><span class="glyphicon glyphicon-th-list"></span> Leaderboard</a></li>
          <li role="presentation"><a href="#"><span class="glyphicon glyphicon-knight"></span> Compete <span style="background-color:red;" class="badge">4</span></a></li>
          <li role="presentation"><a href="#"><span class="glyphicon glyphicon-education"></span> Training</a></li>
          <li>
          <a href="?about=true" class="thumbnail">
            <img src="/tc-img/house.png" style="width:171px;height:180px;" alt="...">
          </a>
          </li>
        </ul>
        </div>
        </div>
      </div>

      <div class="row">
          <div class="col-lg-6">
          <div class="thumbnail"><img src="/tc-img/left_panel.png" alt="..."></div>
          </div>
          <div class="col-lg-6">
          <a href="?about=true" class="thumbnail"><img src="/tc-img/right_panel.png" alt="..."></a>
          </div>
      </div>
      </div>

      <footer class="footer">
        <p>&copy; 2015 Company, Inc.</p>
      </footer>

    </div> <!-- /container -->


        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
      </body>
    </html>
    """

def aboutPage():
    print "</body></html>"

def leaderboardPage():
    print '''<body>
    <div class="container">
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="?home=true">Take Charge</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="?home=true">Home</a></li>
            <li><a href="#">Settings</a></li>
            <li><a href="?profile=true">Profile</a></li>
            <li><a href="?about=true">Help</a></li>
          </ul>
          <form class="navbar-form navbar-right">
            <input type="text" class="form-control" placeholder="Search...">
          </form>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-7 col-sm-offset-3 col-md-8 col-md-offset-2 main">
          <h1 class="page-header">Leaderboard</h1>

          <div class="row placeholders">
          <p style="text-align:left;" class="text-muted">Filters:</p>
            <div class="col-xs-6 col-sm-3 placeholder" style="border: #2c75ff 3px solid;">
              <img src="/tc-img/globe.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Overall</h4>
              <span class="text-muted">You are 246/1233 worldwide</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="/tc-img/nearyou.png" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Near You</h4>
              <span class="text-muted">You are 26/77 in Bondi Beach</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="/tc-img/solarhouse.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Similar Solar</h4>
              <span class="text-muted">You are 101/652 of people with 3kW systems</span>
            </div>
            <div class="col-xs-6 col-sm-3 placeholder">
              <img src="/tc-img/family.jpg" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
              <h4>Similar Household</h4>
              <span class="text-muted">You are 13/90 of families of 4</span>
            </div>
          </div>

          <h2 class="sub-header">Global Leaderboard</h2>
          <nav>
            <ul class="pager">
            <li><a href="#">Previous</a></li>
            <li><a href="#">Next</a></li>
            </ul>
            </nav>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>ChargeScore</th>
                  <th>Energy Made</th>
                  <th>Energy Used</th>
                  <th>Live Weather</th>
                  <th>Win Rate</th>
                  <th>Challenge</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>242</td>
                  <td class="chargeScore">2</td>
                  <td>12</td>
                  <td>-10</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>46%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>243</td>
                  <td class="chargeScore">1.8</td>
                  <td>8</td>
                  <td>-6.2</td>
                  <td><img style="width:30px;" src="/tc-img/rain.png"></td>
                  <td>33%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>244</td>
                  <td class="chargeScore">1.7<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>11.4</td>
                  <td>-9.7</td>
                  <td><img style="width:30px;" src="/tc-img/sunny.png"></td>
                  <td>62%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>245</td>
                  <td class="chargeScore">1.1<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>5.2</td>
                  <td>-4.1</td>
                  <td><img style="width:30px;" src="/tc-img/sunny.png"></td>
                  <td>76%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr style="background-color:#2c75ff;">
                  <td>246</td>
                  <td class="chargeScore">0.5<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>8</td>
                  <td>-7.5</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>55%</td>
                  <td><a class="btn btn-success" disabled='disabled' href="?challenge=247"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>247</td>
                  <td class="chargeScore">0.4</td>
                  <td>18.2</td>
                  <td>-17.8</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>86%</td>
                  <td><a class="btn btn-success" href="?challenge=247"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>248</td>
                  <td class="chargeScore">0.1<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>4.6</td>
                  <td>-4.5</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>90%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>249</td>
                  <td class="chargeScore">0<span style="color:red;" class="glyphicon glyphicon-menu-down"></span></td>
                  <td>12</td>
                  <td>-12</td>
                  <td><img style="width:30px;" src="/tc-img/sunny.png"></td>
                  <td>69%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>250</td>
                  <td class="chargeScore">-1</td>
                  <td>11</td>
                  <td>-12</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>14%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>251</td>
                  <td class="chargeScore">-2.8<span style="color:red;" class="glyphicon glyphicon-menu-down"></span></td>
                  <td>5</td>
                  <td>-7.8</td>
                  <td><img style="width:30px;" src="/tc-img/rain.png"></td>
                  <td>55%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>252</td>
                  <td class="chargeScore">-4<span style="color:red;" class="glyphicon glyphicon-menu-down"></span></td>
                  <td>6.2</td>
                  <td>-10.2</td>
                  <td><img style="width:30px;" src="/tc-img/rain.png"></td>
                  <td>66%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>253</td>
                  <td class="chargeScore">-6.6<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>5</td>
                  <td>-11.6</td>
                  <td><img style="width:30px;" src="/tc-img/rain.png"></td>
                  <td>87%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>254</td>
                  <td class="chargeScore">-6.9<span style="color:red;" class="glyphicon glyphicon-menu-down"></span></td>
                  <td>3</td>
                  <td>-9.9</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>46%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>255</td>
                  <td class="chargeScore">-7.4<span style="color:green;" class="glyphicon glyphicon-menu-up"></span></td>
                  <td>18</td>
                  <td>-25.4</td>
                  <td><img style="width:30px;" src="/tc-img/rain.png"></td>
                  <td>67%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>256</td>
                  <td class="chargeScore">-7.7</td>
                  <td>10</td>
                  <td>-17.7</td>
                  <td><img style="width:30px;" src="/tc-img/sunny.png"></td>
                  <td>55%</td>
                  <td><a class="btn btn-success" href="?challenge=247"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
                <tr>
                  <td>257</td>
                  <td class="chargeScore">-8</td>
                  <td>4</td>
                  <td>-12</td>
                  <td><img style="width:30px;" src="/tc-img/cloudy.png"></td>
                  <td>57%</td>
                  <td><a class="btn btn-success" href="?challenge=258"><span class="glyphicon glyphicon-knight"></span></a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../../dist/js/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="../../assets/js/vendor/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>'''

def challengePage():
    print '''<body>
    <div class="container">
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="?home=true">Take Charge</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="?home=true">Home</a></li>
            <li><a href="#">Settings</a></li>
            <li><a href="?profile=true">Profile</a></li>
            <li><a href="?about=true">Help</a></li>
          </ul>
          <form class="navbar-form navbar-right">
            <input type="text" class="form-control" placeholder="Search...">
          </form>
        </div>
      </div>
    </nav>
        <div class="container-fluid">
            <div class="row">
            <div class="main"><h2><img class="center-block" src="/tc-img/ChallengePage.png" style="height:70vh;"></h2></div>
            </div>
        <form class="form-inline row">
        <div class="col-lg-8">
        <h2 style="text-align:center;">Challenge Byron12:
        <select class="form-control">
          <option>Tomorrow</option>
          <option>11th April</option>
          <option>12th April</option>
          <option>Next Week</option>
        </select>, Odds: <b>$1.80</b>
        </h2>
        <h2 style="text-align:center;">Stake:
        <div class="input-group has-success">
            <span class="input-group-addon">$</span>
            <input type="text" class="form-control"/>
        </div>
        </h2>
        </div>
        <button class="btn btn-primary btn-lg col-lg-3" style="margin-top:5%;">Send Challenge</button>
        </form>
        </div>

    </div>
    </body>
    </html>

    '''

if "home" in parameters.keys():
    homePage()
elif "about" in parameters.keys():
    aboutPage()
elif "leaderboard" in parameters.keys():
    leaderboardPage()
elif "challenge" in parameters.keys():
    challengePage()
elif "profile" in parameters.keys():
    profilePage()
else:
    print """
          <form method="POST" class="form-signin" action="?home=true">
            <h2 class="form-signin-heading">Please sign in</h2>
            <label for="inputEmail" class="sr-only">Username</label>
            <input type="text" id="inputEmail" name="inputEmail" class="form-control" placeholder="Username" required autofocus>
            <label for="inputPass" class="sr-only">Password</label>
            <input type="password" id="inputPass" name="inputPass" class="form-control" placeholder="Password" required>
            <div class="checkbox">
              <label>
                <input type="checkbox" value="remember-me"> Remember me
              </label>
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
          </form>

        </div> <!-- /container -->


        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
      </body>
    </html>
    """


'''
def loggedIn():
    if environ.has_key('HTTP_COOKIE'):
        # loop through cookies
        for cookie in map(strip,split(environ['HTTP_COOKIE'],';')):
            (key, value) = split(cookie,'=')
            if key == "User":
                return True
    return False

def main():
    C = Cookie.SimpleCookie()
    parameters = cgi.FieldStorage()
    if (!loggedIn()):
        if ("inputEmail" in parameters):
            inputEmail = parameters["inputEmail"].value
        else:
            inputEmail = "boop"
        if ("inputPass" in parameters):
            inputPass = parameters["inputPass"].value
        else:
            inputPass = "boop"
        f = open('users.txt','r')
        users = {}
        lines = f.readlines()
        for line in lines:
            data = line.split()
            user = data[0]
            password = data[1]
            users[user] = password
        if inputEmail in users.keys():
            if inputPass == users[inputEmail]:
                loggedIn = True
                print "Set-Cookie:User="+inputEmail+";\r\n"
    f.close()
    print "Content-type: text/html"
    print ""
    print """
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="/tc-img/logo-blue-face.png">

        <title>Take Charge</title>

        <!-- Bootstrap core CSS -->
        <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
        <link href="/bootstrap/css/signin.css" rel="stylesheet">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>

      <body>

        <div class="container">
        """
print """
          <form method="POST" class="form-signin">
            <h2 class="form-signin-heading">Please sign in</h2>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" id="inputEmail" name="inputEmail" class="form-control" placeholder="Email address" required autofocus>
            <label for="inputPass" class="sr-only">Password</label>
            <input type="password" id="inputPass" name="inputPass" class="form-control" placeholder="Password" required>
            <div class="checkbox">
              <label>
                <input type="checkbox" value="remember-me"> Remember me
              </label>
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
          </form>

        </div> <!-- /container -->


        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
      </body>
    </html>
    """
main()
'''