#!"C:\xampp\perl\bin\perl.exe"
print "Content-type: text/html; charset=UTF-8\n\n";

use CGI;
use DBI;
use strict;
use warnings;
use utf8;


print <<'INIT_PAGE';
<!doctype html>
<html lang="ja">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Bootstrap v5.2_cgi_sample</title>

		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">


		<style>
			.bd-placeholder-img {
				font-size: 1.125rem;
				text-anchor: middle;
				-webkit-user-select: none;
				-moz-user-select: none;
				user-select: none;
			}

			@media (min-width: 768px) {
				.bd-placeholder-img-lg {
					font-size: 3.5rem;
				}
			}

			.b-example-divider {
				height: 3rem;
				background-color: rgba(0, 0, 0, .1);
				border: solid rgba(0, 0, 0, .15);
				border-width: 1px 0;
				box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
			}

			.b-example-vr {
				flex-shrink: 0;
				width: 1.5rem;
				height: 100vh;
			}

			.bi {
				vertical-align: -.125em;
				fill: currentColor;
			}

			.nav-scroller {
				position: relative;
				z-index: 2;
				height: 2.75rem;
				overflow-y: hidden;
			}

			.nav-scroller .nav {
				display: flex;
				flex-wrap: nowrap;
				padding-bottom: 1rem;
				margin-top: -1px;
				overflow-x: auto;
				text-align: center;
				white-space: nowrap;
				-webkit-overflow-scrolling: touch;
			}
			.top{
				vertical-align:top;
				}
			.middle{
				vertical-align:middle;
			}
			.bottom{
				vertical-align:bottom;
			}
			.left{
				text-align: left;
			}
			.center{
				text-align: center;
			}
			.right{
				text-align: right;
			}
			.empty_cell {
				empty-cells: hide;
			}
			.icon_bootstrap {
				vertical-align: -.125em;
				fill: #7b56b3;
				width: 32px;
				height: 32px;
			}
			.icon_perl {
				vertical-align: -.125em;
				fill: #4fc4ff;
				width: 32px;
				height: 32px;
			}
			table{
				border-collapse: separate;
			}
			p {
			overflow-wrap: break-word;
			}
		</style>


		<!-- Custom styles for this template -->
		<link href="css/bbs.css" rel="stylesheet">
	</head>
<body>


<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
	<symbol id="bootstrap" viewBox="0 0 118 94">
		<path fill-rule="evenodd" clip-rule="evenodd" d="M24.509 0c-6.733 0-11.715 5.893-11.492 12.284.214 6.14-.064 14.092-2.066 20.577C8.943 39.365 5.547 43.485 0 44.014v5.972c5.547.529 8.943 4.649 10.951 11.153 2.002 6.485 2.28 14.437 2.066 20.577C12.794 88.106 17.776 94 24.51 94H93.5c6.733 0 11.714-5.893 11.491-12.284-.214-6.14.064-14.092 2.066-20.577 2.009-6.504 5.396-10.624 10.943-11.153v-5.972c-5.547-.529-8.934-4.649-10.943-11.153-2.002-6.484-2.28-14.437-2.066-20.577C105.214 5.894 100.233 0 93.5 0H24.508zM80 57.863C80 66.663 73.436 72 62.543 72H44a2 2 0 01-2-2V24a2 2 0 012-2h18.437c9.083 0 15.044 4.92 15.044 12.474 0 5.302-4.01 10.049-9.119 10.88v.277C75.317 46.394 80 51.21 80 57.863zM60.521 28.34H49.948v14.934h8.905c6.884 0 10.68-2.772 10.68-7.727 0-4.643-3.264-7.207-9.012-7.207zM49.948 49.2v16.458H60.91c7.167 0 10.964-2.876 10.964-8.281 0-5.406-3.903-8.178-11.425-8.178H49.948z"></path>
	</symbol>
	<symbol id = "Perl" viewBox="0 0 32 32" width="32" height="32">
		<path d="M30.642 15.77s-.5-.607-.58-1.374.286-.5.286-.5-.143-1.018-.858-1.893-1.482-1.91-1.82-3.286-.964-2.178-1.393-2.732-.607-1.643-.858-2.036S25.132 1.386 23.33.4s-5.09.147-6.054.826-1.84 2.643-3 3.447-2.107.82-3.036 2.41-1.125 2.5-1.08 3.428c0 0-.67.08-.75-.294s.188-1.634.375-2.01c0 0 .188.16.16.322 0 0 .563-1.152.214-1.848 0 0 .188.04.28.134 0 0 .228-1.085.228-1.794s-.268-1.26-.737-1.58c0 0 .35-.455-.04-.95 0 0-.174-.398-.63-.87S8.46.872 8 .886c0 0 .08-.174.16-.28 0 0-.39.046-.523.224 0 0-.214-.13-.254-.438 0 0-.375.107-.416.375 0 0-.826-.28-1.178.616 0 0 .134.053.174.147 0 0-.12.268-.643.308s-2.023 0-2.477.16-.643.322-.643.51c0 0-.228.107-.335.603 0 0-.356.174-.356.482s.196.22.196.22-.214.612.536.652c0 0 .12.308.764.308s1.11.107 1.38.51c0 0-.214.804-1.058 1.54a2.02 2.02 0 0 0 .375.014s-.737.616-.924 1.513c0 0 .255-.254.402-.24 0 0-.924 2.558.362 5.09 0 0 .12-.254.174-.28 0 0-.053.858.47 1.527 0 0 .04-.375.24-.51 0 0 .803 1.46 1.627 2.116s2.083.964 2.364 1.634c0 0 .442-.494.442-.816 0 0 .12.307.08.628 0 0 .496-.24.656-.374s.858-.616.95.16-.687 2.33.027 4.26c0 0-.25.35-.25.818s.357.7.357.914-.16.608-.16 1.018.375 1.067.036 2.533-.482 1.86-.68 2.11-.964.68-.82 1.393c0 0-1.803.232-1.786.857s.93.82 2.018.82 1.374-.23 1.4-.624-.25-.465 0-.696.52-.5.483-1.482.446-1.893.446-1.893-.09-.84.197-1.357 1.053-1.536.536-3.09c0 0 .142.054.32.07 0 0-.304-.857.25-1.893s.84-3.143.84-3.143 1.268.108 1.82 0c0 0-1.214 2.545-1.09 4.46 0 0-.304.307-.304.646s.18.767.482 1.07 1.304.91 1.857 1.57.93 1.392 1.09 1.59c0 0-.517.34-.375.875 0 0-.518.16-.464.607 0 0-.75.018-1.143.358s-.59.786-.232.928 1.68.143 2.125.143.964-.34 1-.57-.16-.804-.16-.804.268.036.375-.286c0 0 .5 1.857 1.268 1.803 0 0 .107-.017.125-.178 0 0 .357.09.536-.09s.607-2.696-.91-2.733c0 0 .107-.25-.18-.428s2.5-3.696 2.82-4c0 0-.393-3.142.393-4.66l1.428-2.554s.16 3.375 1.696 5.964a1.31 1.31 0 0 0 .214.875c-.07.482-.267.732-.267 1.34s.446 2.214.017 3.964c-.086.35-.946 1.393-.642 2.25 0 0-.714.41-.714.947s.32.643.554.643.357-.232.482-.232.304.34.875.34 1.07-.464 1.07-.732-.464-.714-.464-.714.304-.286.304-.642-.482-.946-.482-1.696.156-2.206.446-2.84c.58-1.268.518-2.277.18-2.544 0 0 .178-.812.178-1.67s-.66-3.152-.107-5.464c0 0 .66-.964.804-2.482 0 0 1.196 2.43.303 4.125s-.714 1.68-.732 2.196.25 1.233.25 1.233L29 19.68s-.01-.57.383-.982.68-1.526.5-1.834l.286.21s.143-.536-.125-1.32c0 0 .287-.143.6.017zM19.92 23.805l-1.375 2.214s-1.072-.607-1.41-1.286-.625-1.107-.768-1.214c0 0 .437-.59.544-1.214 0 0 .192.015.3.4.65-.816 1.073-1.7 1.192-2.63 0 0 .16.16.304.214 0 0 .017-.643.25-1.107s.732-1.054.804-1.947h.32s-.268 2 0 3.714.178 2.32-.16 2.857z"/>
	</symbol>
	<symbol id="search" viewBox="0 0 16 16">
		<path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
	</symbol>
	<symbol id="submit" viewBox="0 0 16 16">
		<path fill-rule="evenodd" d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0v-2z"/>
		<path fill-rule="evenodd" d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
	</symbol>
	<symbol id="trash" viewBox="0 0 16 16">
		<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
		<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
	</symbol>
</svg>


<main>
	<h1 class="visually-hidden">Bootstrap webpage</h1>
	<div class="px-3 py-2 bg-dark">
		<div class="container">
			<nav class="navbar text-light justify-content-center">
				<div class="d-flex">
					<svg class="icon_bootstrap me-2" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"/></svg>
					<svg class="icon_perl me-2" role="img" aria-label="Perl"><use xlink:href="#Perl"/></svg>
					初めての Bootstrap & Perl_CGI webページ
				</div>
			</nav>
		</div>
	</div>

	<div class="px-3 py-2 mb-3">
		<div class="d-flex flex-nowrap justify-content-center">
			<form method="post" class="container mb-2" action="bbs.cgi">
				<div class="row align-items-center mt-1">
					<div class="col-2">
						<b>名前</b>
					</div>
					<div class="col-10">
						<input type="text" class="form-control" placeholder="名前を入力してください" name="string_client_name">
					</div>
				</div>
				<div class="row align-items-center mt-1">
					<div class="col-2">
						<b>メッセージ</b>
					</div>
					<div class="col-10">
						<textarea type="text" class="form-control" placeholder="文字を入力してください" name="string_client_entered" rows="4"></textarea>
					</div>
				</div>
				<div class="row mt-1">
					<div class="col-2">
					</div>
					<div class="col-10">
						<button type="submit" class="btn btn-primary">
						送信 <svg class="submit" width="24" height="24" fill="currentColor"><use xlink:href="#submit"/></svg>
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</main>
<hr>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>


INIT_PAGE

my $query = CGI->new;
my $name = $query->param('string_client_name');
my $message = $query->param('string_client_entered');

sub disable_tag_char {
		my $str = shift @_;
		$str =~ s/</&lt;/g;
		$str =~ s/>/&gt;/g;
		return $str;
}

# DB 接続, テーブル作成
my $dbh = DBI->connect("dbi:SQLite:dbname=msg.db");
$dbh->do("create table msg_log(name, message, time, id);");

# DB へデータを格納
if ($message ne "") {
	# タグの無効化
	$name = disable_tag_char($name);
	$message = disable_tag_char($message);

	$message =~ s/\r\n/<br>/g; # Windows系
	$message =~ s/\r/<br>/g; # Mac系
	$message =~ s/\n/<br>/g; # Unix系

	# idを設定する (データベースに情報がある → 取得したデータの id の最大値 + 1" を設定する, データベースに情報がない → "1"を設定する)
	my $id = 1;
	my $sth_fetchid = $dbh->prepare("select * from msg_log");
	$sth_fetchid->execute;
	while (my @row = $sth_fetchid->fetchrow_array) {
		if (defined $id) {
			if ($id >= $row[3]) {
				# 取り出した id の中から最大値 + 1 の値を設定する
				$id = $row[3] + 1;
			}
		} else {
			# 要素無しのため、何もしない( id は "1" のまま)
		}
	}
	$sth_fetchid->finish;
	undef $sth_fetchid;

	my $insert_msg = sprintf ("insert into msg_log (name, message, time, id) values ('$name', '$message', datetime('now', 'localtime'), '$id');");
	$dbh->do($insert_msg);
}

# テーブルの読み出し命令
my $sth = $dbh->prepare("select * from msg_log");
$sth->execute;

# 各データを展開し、配列へ格納
while(my @log = $sth->fetchrow_array) {
	# chompを使うと正しく表示されない
	my ($n, $m, $t, $i) = @log;

	# 時間のフォーマット変更 (2022-10-10 → 2022/10/10)
	$t =~ s/-/\//g;

print <<"MESSAGE_BOX";
<div class="container mb-1 rounded-3" style="border: 2px solid #000000">
	<div class="row align-items-center">
		<div class="col-auto">
			$t
		</div>
		<div class="col-auto">
			by $n
		</div>
		<div class="col-auto ms-auto">
			ID : "$i"
		</div>
		<div class="col-auto">
			<button type="button" class="btn btn-outline-primary mt-1">
				<svg class="trash" width="20" height="20" fill="currentColor"><use xlink:href="#trash"/></svg>
			</button>
		</div>
	</div>
	<div class="container mb-2 mt-1" style="border: 2px solid grey">
		<p>$m</p>
	</div>
</div>\n
MESSAGE_BOX

}
$sth->finish;
undef $sth;

print "</body>\n</html>\n";

# DB 切断
$dbh->disconnect;
