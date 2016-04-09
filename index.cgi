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
if ("home" in parameters):
    print """
        <!-- Custom styles for this template -->
        <link href="/bootstrap/css/jumbotron-narrow.css" rel="stylesheet">
        <link href="/bootstrap/css/style.css" rel="stylesheet">
    """
else:
    print """
        <!-- Custom styles for this template -->
        <link href="/bootstrap/css/signin.css" rel="stylesheet">
    """
print """
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>

      <body>
      <div class="container">
        """

def homePage():
    rating = -18
    if (rating < -50):
        buttonType = "danger"
    elif (rating > -50 and rating < -15):
        buttonType = "warning"
    elif (rating > -15 and rating < 0):
        buttonType = "info"
    else:
        buttonType = "success"
    print """
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" class="active"><a href="#">Home</a></li>
            <li role="presentation"><a href="#">About</a></li>
            <li role="presentation"><a href="#">Contact</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">Take Charge</h3>
      </div>
      <div class="jumbotron">
        <div class="row">
        <div class="col-lg-6" style="text-align:right;">
        <span style="font-size:20px;">Consumption: </span><div style="display:inline-block" class="circle-red">40</div>
        <div style="margin-top:10px;"></div>
        <span style="font-size:20px;">Generation: </span><div style="display:inline-block" class="circle-green">30</div>
        <div style="margin-top:30px;"></div>
        <p>Score: <a class="btn btn-lg btn-"""+buttonType+"""" href="#" role="button">"""+str(rating)+"""</a></p>
        </div>
        <div class="sidemain col-lg-offset-1 col-lg-5">
        <ul class="nav nav-pills nav-stacked">
          <li role="presentation"><a href="#"><span class="glyphicon glyphicon-th-list"></span> Leaderboard</a></li>
          <li role="presentation"><a href="#"><span class="glyphicon glyphicon-knight"></span> Compete</a></li>
          <li role="presentation"><a href="#"><span class="glyphicon glyphicon-education"></span> Training</a></li>
          <li>
          <a href="#" class="thumbnail">
            <img src="/tc-img/house.png" style="width:171px;height:180px;" alt="...">
          </a>
          </li>
        </ul>
        </div>
        </div>
      </div>
      </div>
      <div class="row marketing">
        <div class="col-lg-6">
          <h4>Subheading</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Subheading</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Subheading</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>

        <div class="col-lg-6">
          <h4>Subheading</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Subheading</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Subheading</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
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

if "home" in parameters.keys():
    homePage()
else:
    print """
          <form method="POST" class="form-signin" action="?home=true">
            <h2 class="form-signin-heading">Please sign in</h2>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="text" id="inputEmail" name="inputEmail" class="form-control" placeholder="Email address" required autofocus>
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