# Comandos de la Práctica 01
## Daniel Enrique Acosta García

### Parte 1

**Respuesta 1:**

echo $SHELL
/bin/bash 

**Respuesta 2:**

mkdir {data,filtered,raw_data,meta,scripts,figures,archive}

**Respuesta 3:**

mv {raw_data,filtered} data

**Respuesta 4:**

La organización de los directorios empleada simula la forma en que usualmente se estructuran los archivos relacionados con un proyecto bioinformático para facilitar su acceso y su reproducibilidad.


### Parte 2

**Respuesta 1:**

cd scripts/
chmod a+x delay.sh


**Respuesta 2:**

ls -l 

-rwxrwxr-x. 1 dacosta dacosta  127 Oct 28 03:36 delay.sh


./delay.sh


**Respuesta 3:**

sleep 30

**Respuesta 4:**

sleep 300&
[3] 5242

kill -9 5242
[3]+  Killed                  sleep 300


### Parte 3

**Respuesta 1:**

cd ../meta/
cd

nano SarsCov-2.txt

wc -w SarsCov-2.txt 
122 SarsCov-2.txt


**Respuesta 2:**

cd ..
mv /home/dacosta/Downloads/sequence* ./data/raw_data
cd data/raw_data
mv sequence.gff3 sarscov2_genome.gff3
mv sequence.fasta sarscov2_genome.fasta
mv sequence\(1\).fasta splike_c.faa
mv sequence\(2\).fasta splike_b.faa
mv sequence\(3\).fasta splike_a.faa
mv /home/dacosta/Downloads/S* . 
mv /home/dacosta/Downloads/sarscov2_assembly.fasta.gz . 


### Parte IV

**Respuesta 1:**
ln -s ../raw_data/splike_a.faa 
ln -s ../raw_data/splike_b.faa 
ln -s ../raw_data/splike_c.faa 

**Respuesta 2:**

touch glycoproteins.faa

**Respuesta 3:**

grep ">" * 
splike_a.faa:>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein
splike_b.faa:>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein
splike_c.faa:>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein

**Respuesta 4:**

cat sp* > glycoproteins.faa

**Respuesta 5:**

mv ../raw_data/splike_* ../../archive/

Las ligas simbólicas en raw_data se rompieron. Se tornaron de color rojo al observarlas con "ls" y no es posible abrirlas debido a que estan enlazadas con la dirección original de los archivos, ahora inexistente.

**Respuesta 6:**

cd ../raw_data/
less sarscov2_genome.fasta
zless sarscov2_assembly.fasta.gz

head -3 sarscov2_genome.fasta 
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

zcat sarscov2_assembly.fasta.gz | head -3
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG


**Respuesta 7:**

grep ">" sarscov2_genome.fasta | wc -l >> ../../comandos_p01.md 
zcat sarscov2_assembly.fasta.gz | grep ">" | wc -l >> ../../comandos_p01.md 


1

35

**Respuesta 8:**

zcat SRR10971381_R2.fastq.gz | head -12 >> ../../comandos_p01.md 

@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF

zcat SRR10971381_R2.fastq.gz | grep "@" | wc -l >> ../../comandos_p01.md 
130022

**Respuesta 9:**

El formato ".faa" se ocupa para secuencias de aminoácidos, "fasta" para secuencias de nucleótidos y "fastqc" para secuencias de nucleótidos asociadas a un valor de calidad proveniente de la secuenciación.

**Respuesta 10:**

La opción "-S" desplega una versión estructurada de el archivo a manera de tabla.

**Respuesta 11:**

awk '$3=="gene"' sarscov2_genome.gff3 | wc -l
11

El tercer campo de los archivos ".gff" se refiere al tipo con el que se caracteriza a la secuencia. La diferencia entre "CDS" y "gene" radica en que la primera sólo incluye la región exónica o codificante mientras que la última presenta la secuencia del gen completo.

### Ejercicio extra

**Respuesta 1:**

cd ../../figures/
ln -s ../data/raw_data/sarscov2-genome.gff3

**Respuesta 2:**

cat sarscov2_genome.gff3 | grep -v &quot;^#&quot; | cut -f 3 | sort | uniq -c >> barplotdata.txt
      1 
     13 CDS
      1 five_prime_UTR
     11 gene
     27 mature_protein_region_of_CDS
      1 region
      5 stem_loop
      1 three_prime_UTR

8 categorías

