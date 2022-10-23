# Adatok:
param k; # jegyek száma
param n; # számjegyek száma

param s{1..k}; # üzem termelése
param d{1..n}; # fogyasztó igényei
param c{1..k, 1..n}; # útvonal kapacitás
param f{1..k, 1..n}; # szállítási költség egy adott útvonalon

# Változók: k*n db változó bevezetése:
# Jelentése: Mennyit szállítunk i és j pont között?
var x{1..k, 1..n} >= 0;


# Feltételek

# k db feltétel bevezetése a fogyasztásra
# Egyik üzem sem termelhet többet a kapacitásnál
subject to sup{i in 1..k}: sum{j in 1..n} x[i,j] <= s[i];

# n db feltétel bevezetése a kiszolgáláshoz
# Minden fogyasztóhoz érkezzen meg a szükséges mennyiség
# Megj: Lehetne >= is, de a megoldáson nem változtatna!
s.t. dem{j in 1..n}: sum{i in 1..k} x[i,j] = d[j];

# k*n db feltétel bevezetése a szállításhoz
# Minden útvonalon max annyit szállíthatunk, amennyi annak a kapacitása!
cap{i in 1..k, j in 1..n}: x[i,j] <= c[i,j];

# Célfüggvény
# A fenti feltételek függvényében hogyan lehetne a legolcsóbban kiszolgálni a fogyasztókat?
minimize cost: sum{i in 1..k, j in 1..n} f[i,j] * x[i,j];

# Ellenõrzés: A teljes fogyasztás ne legyen nagyobb, mint a gyártási képesség
# Ha ez elbukik, rögtön dobjon hibát!
check sum{j in 1..n} d[j] < sum{i in 1..k} s[i];

# Megoldás keresése
option solver cplex;
solve;


printf "\n\n\n";

# Eredmény kiírása
# Ez valójában egy dupla for-ciklus!
for {i in 1..k, j in 1..n} {
	# printf "minta", változók[]
	# A minta egy if then else szerkezet
	printf (if (x[i,j] > 0) then "Uzem: %2d, Fogy: %2d, Menny: %4d \n" else ""), i, j, x[i,j];
}

# Célfüggvény eredménye
printf "Osszkoltseg: %d\n", cost;

printf "\n\n\n";


# Adat rész
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

# kapacitás listásan megadása
param c :=
		1	1	0
		1	2	200
		1	3	200
		1	4	100
		2	1	100
		2	2	450
		2	3	1000
		2	4	200;

# költség mátrixosan megadva
param f default 100 (tr)
	 :		1		2 :=
	 1		.		160
	 2		.		180
	 3		60		90
	 4		160		190	;

end;
