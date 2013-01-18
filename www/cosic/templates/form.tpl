<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset=utf-8>
    <title>COSIC logo generator</title>
    <link rel="stylesheet" href="http://meyerweb.com/eric/tools/css/reset/reset.css" type="text/css" media="screen" charset="utf-8">
    <style type="text/css" media="screen">
        body {
            padding: 30px;
        }
        div {
            float: left;
            width: 50%;
        }
        form {
            float: right;
            width: 50%;
        }
        h1 {
            font-weight: bold;
            margin-bottom: 1em;
        }
    </style>
</head>
<body>

    <div>
        <p>
            <img src="/logo.png" />
            <img src="/logo.png" style="height: 115px; width:92px" />
        <p>
        <p>
        <a id="epslink" href="/logo.eps">Download as .EPS (prefered: dynamic version, for print)</a>
        </p>
        <p>
        <a id="pnglink" href="/logo.png">Download as .PNG (static version, for web)</a>
        </p>
    </div>

    <form method="post" action=".">
        <h1>COSIC Logo Generator</h1>
        <p>
        <label for="color">color</label><br />
        <input type="color" name="color">
        </p>

        <p>
        <label for="period">period</label><br />
        <input step="0.1" min="1" max="5" value="2.1" type="range" name="period">
        </p>

        <p>
        <label for="thickness">thickness</label><br />
        <input step="0.1" min="0.3" max="2" value="0.7" type="range" name="thickness">
        </p>

        <!--<p>-->
        <!--<label for="format">format</label><br />-->
        <!--<select name="format">-->
            <!--<option selected="selected" value="eps">EPS: Encapsulated Postscript (prefered)</option>-->
            <!--<option value="png">PNG: Portable Network Graphics (for web use)</option>-->
        <!--</select>-->
        <!--</p>-->
        
        <!--<p>-->
        <!--<input type="submit" value="Submit">-->
        <!--</p>-->
    </form>


    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>
    $(function() {
        var $form = $("form"),
            $img = $("img"),
            $pnglink = $("#pnglink"),
            $epslink = $("#epslink"),
            timer;
        
        function refresh () { 
            qs = $form.serialize()
            $img.attr("src", "/logo.png?" + qs);
            $pnglink.attr("href", "/logo.png?download=true&" + qs);
            $epslink.attr("href", "/logo.eps?download=true&" + qs);
        };

        $("input,label").change(function() {
            if(timer) {
                clearTimeout(timer);
            }
            timer = setTimeout(refresh, 500);
        });
    });
    </script>
</body>
</html>
