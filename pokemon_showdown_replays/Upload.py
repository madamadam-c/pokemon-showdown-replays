from datetime import datetime


def upload_replay_start(replay: dict, client_location: str = "https://play.pokemonshowdown.com"):
    html = f"""<!DOCTYPE html>
<html><head>

	<meta charset="utf-8" />

	<title>{replay['format']} replay: {replay['p1']} vs. {replay['p2']} - Pok&eacute;mon Showdown</title>

	<meta name="description" content="Watch a replay of a Pokémon battle between {replay['p1']} and {replay['p2']} ({replay['format']})" />

	<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=IE8" />
	<link rel="stylesheet" href="https://{client_location}/style/font-awesome.css?932f42c7" />
	<link rel="stylesheet" href="https://pokemonshowdown.com/theme/panels.css?0.8626627733285226" />
	<link rel="stylesheet" href="https://pokemonshowdown.com/theme/main.css?0.9739025453096699" />
	<link rel="stylesheet" href="https://{client_location}/style/battle.css?8e37a9fd" />
	<link rel="stylesheet" href="https://{client_location}/style/replay.css?cfa51183" />
	<link rel="stylesheet" href="https://{client_location}/style/utilichart.css?e39c48cf" />
	<!-- Workarounds for IE bugs to display trees correctly. -->
	<!--[if lte IE 6]><style> li.tree {{ height: 1px; }} </style><![endif]-->
	<!--[if IE 7]><style> li.tree {{ zoom: 1; }} </style><![endif]-->

</head><body>

	<div class="pfx-topbar">
		<div class="header">
			<ul class="nav">
				<li><a class="button nav-first" href="https://pokemonshowdown.com/?0.03188637145193396"><img src="https://pokemonshowdown.com/images/pokemonshowdownbeta.png?0.02847646698151296" alt="Pok&eacute;mon Showdown! (beta)" /> Home</a></li>
				<li><a class="button" href="https://dex.pokemonshowdown.com/?0.5521979938481671">Pok&eacute;dex</a></li>
				<li><a class="button cur" href="/?0.5977172940377489">Replays</a></li>
				<li><a class="button" href="https://pokemonshowdown.com/ladder/?0.5868977915492632">Ladder</a></li>
				<li><a class="button nav-last" href="https://pokemonshowdown.com/forums/?0.0327954326633102">Forum</a></li>
			</ul>
			<ul class="nav nav-play">
				<li><a class="button greenbutton nav-first nav-last" href="http://play.pokemonshowdown.com/">Play</a></li>
			</ul>
			<div style="clear:both"></div>
		</div>
	</div>
	<div class="pfx-panel"><div class="pfx-body" style="max-width:1180px">
		<div class="wrapper replay-wrapper">

			<div class="battle"><div class="playbutton"><button disabled>Loading...</button></div></div>
			<div class="battle-log"></div>
			<div class="replay-controls">
				<button data-action="start"><i class="fa fa-play"></i> Play</button>
			</div>
			<div class="replay-controls-2">
				<div class="chooser leftchooser speedchooser">
					<em>Speed:</em>
					<div><button value="hyperfast">Hyperfast</button> <button value="fast">Fast</button><button value="normal" class="sel">Normal</button><button value="slow">Slow</button><button value="reallyslow">Really Slow</button></div>
				</div>
				<div class="chooser colorchooser">
					<em>Color&nbsp;scheme:</em>
					<div><button class="sel" value="light">Light</button><button value="dark">Dark</button></div>
				</div>
				<div class="chooser soundchooser" style="display:none">
					<em>Music:</em>
					<div><button class="sel" value="on">On</button><button value="off">Off</button></div>
				</div>
			</div>
			<!--[if lte IE 8]>
				<div class="error"><p>&#3232;_&#3232; <strong>You're using an old version of Internet Explorer.</strong></p>
				<p>We use some transparent backgrounds, rounded corners, and other effects that your old version of IE doesn't support.</p>
				<p>Please install <em>one</em> of these: <a href="http://www.google.com/chrome">Chrome</a> | <a href="http://www.mozilla.org/en-US/firefox/">Firefox</a> | <a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home">Internet Explorer 9</a></p></div>
			<![endif]-->

			
			<pre class="urlbox" style="word-wrap: break-word;">https://replay.pokemonshowdown.com/{replay['id'].split("battle-")[1]}</pre>

			<h1 style="font-weight:normal;text-align:left"><strong>{replay['format']}</strong>: <a href="https://pokemonshowdown.com/users/{replay['p1']}" class="subtle">{replay['p1']}</a> vs. <a href="https://pokemonshowdown.com/users/{replay['p2']}" class="subtle">{replay['p2']}</a></h1>
			<p style="padding:0 1em;margin-top:0">
				<small class="uploaddate" data-timestamp="{replay['timestamp']}"><em>Uploaded:</em> {datetime.fromtimestamp(replay['timestamp']).strftime("%m/%d/%Y %H:%M:%S")}</small>
			</p>

			<div id="loopcount"></div>
		</div>

		<input type="hidden" name="replayid" value="{replay['id'].split("battle-")[1]}" />

		<script type="text/plain" class="log">"""
    
    return html

def upload_replay_end(client_location: str = "https://play.pokemonshowdown.com"):
    return f"""</script>



		<a href="/index.php" class="pfx-backbutton" data-target="back"><i class="fa fa-chevron-left"></i> Other replays</a>

	</div></div>
	<script src="{client_location}/js/lib/jquery-1.11.0.min.js"></script>
	<script src="{client_location}/js/lib/lodash.core.js"></script>
	<script src="{client_location}/js/lib/backbone.js"></script>
	<script src="https://dex.pokemonshowdown.com/js/panels.js"></script>

	<script src="{client_location}/js/lib/jquery-cookie.js"></script>
	<script src="{client_location}/js/lib/html-sanitizer-minified.js"></script>
	<script src="{client_location}/js/battle-sound.js"></script>
	<script src="{client_location}/config/config.js"></script>
	<script src="{client_location}/js/battledata.js"></script>
	<script src="{client_location}/data/pokedex-mini.js"></script>
	<script src="{client_location}/data/pokedex-mini-bw.js"></script>
	<script src="{client_location}/data/graphics.js"></script>
	<script src="{client_location}/data/pokedex.js"></script>
	<script src="{client_location}/data/items.js"></script>
	<script src="{client_location}/data/moves.js"></script>
	<script src="{client_location}/data/abilities.js"></script>
	<script src="{client_location}/data/teambuilder-tables.js"></script>
	<script src="{client_location}/js/battle-tooltips.js"></script>
	<script src="{client_location}/js/battle.js"></script>
	<script src="{client_location}/replays/js/replay.js"></script>

</body></html>
"""

def create_replay(replay: dict, client_location = "https://play.pokemonshowdown.com"): # the type of replay at https://replay.pokemonshowdown.com/
    start = upload_replay_start(replay, client_location = client_location)
    log = replay['log']
    end = upload_replay_end(client_location = client_location)

    return start + log + end