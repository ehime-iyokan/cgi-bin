use strict;
use warnings;
use utf8;
use DBI;

my $dbh = DBI->connect("dbi:SQLite:dbname=msg.db");

chmod (0777, "msg.db");

# memo : createはtable作成時のみ実行
$dbh->do("create table msg_log(name, message);");

$dbh->do("insert into msg_log (name, message) values ('init_n', 'init_m');");

my $sth = $dbh->prepare("select * from msg_log");
$sth->execute;

while (my @row = $sth->fetchrow_array) {
	print "$row[0],$row[1]\n";
}
$sth->finish;
undef $sth;

$dbh->disconnect;
