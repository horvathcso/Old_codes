# Adatok:
param k; # jegyek sz�ma
param n; # sz�mjegyek sz�ma

param s{1..k}; # �zem termel�se
param d{1..n}; # fogyaszt� ig�nyei
param c{1..k, 1..n}; # �tvonal kapacit�s
param f{1..k, 1..n}; # sz�ll�t�si k�lts�g egy adott �tvonalon

# V�ltoz�k: k*n db v�ltoz� bevezet�se:
# Jelent�se: Mennyit sz�ll�tunk i �s j pont k�z�tt?
var x{1..k, 1..n} >= 0;


# Felt�telek

# k db felt�tel bevezet�se a fogyaszt�sra
# Egyik �zem sem termelhet t�bbet a kapacit�sn�l
subject to sup{i in 1..k}: sum{j in 1..n} x[i,j] <= s[i];

# n db felt�tel bevezet�se a kiszolg�l�shoz
# Minden fogyaszt�hoz �rkezzen meg a sz�ks�ges mennyis�g
# Megj: Lehetne >= is, de a megold�son nem v�ltoztatna!
s.t. dem{j in 1..n}: sum{i in 1..k} x[i,j] = d[j];

# k*n db felt�tel bevezet�se a sz�ll�t�shoz
# Minden �tvonalon max annyit sz�ll�thatunk, amennyi annak a kapacit�sa!
cap{i in 1..k, j in 1..n}: x[i,j] <= c[i,j];

# C�lf�ggv�ny
# A fenti felt�telek f�ggv�ny�ben hogyan lehetne a legolcs�bban kiszolg�lni a fogyaszt�kat?
minimize cost: sum{i in 1..k, j in 1..n} f[i,j] * x[i,j];

# Ellen�rz�s: A teljes fogyaszt�s ne legyen nagyobb, mint a gy�rt�si k�pess�g
# Ha ez elbukik, r�gt�n dobjon hib�t!
check sum{j in 1..n} d[j] < sum{i in 1..k} s[i];

# Megold�s keres�se
option solver cplex;
solve;


printf "\n\n\n";

# Eredm�ny ki�r�sa
# Ez val�j�ban egy dupla for-ciklus!
for {i in 1..k, j in 1..n} {
	# printf "minta", v�ltoz�k[]
	# A minta egy if then else szerkezet
	printf (if (x[i,j] > 0) then "Uzem: %2d, Fogy: %2d, Menny: %4d \n" else ""), i, j, x[i,j];
}

# C�lf�ggv�ny eredm�nye
printf "Osszkoltseg: %d\n", cost;

printf "\n\n\n";


# Adat r�sz
data;

# k, n, s, d
param k := 16;
param n := 10;
param s :=
	1 200
	2 1400;

param d :=
	1 40
	2 500
	3 300
	4 250;

# kapacit�s list�san megad�sa
param c :=
		1	1	0
		1	2	200
		1	3	200
		1	4	100
		2	1	100
		2	2	450
		2	3	1000
		2	4	200;

# k�lts�g m�trixosan megadva
param f default 100 (tr)
	 :		1		2 :=
	 1		.		160
	 2		.		180
	 3		60		90
	 4		160		190	;

end;
