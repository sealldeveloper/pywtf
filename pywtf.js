function $(id){
  return document.getElementById(id);
}

const csvData = `0,chr(int())
1,chr(not())
2,chr(len(str(dict())))
3,chr(len(hex(int())))
4,chr(len(str(not())))
5,chr(len(str(set())))
6,chr(len(str(complex(not()))))
7,chr(len(repr(str(set()))))
8,chr(len(bin(ord(str(int())))))
9,chr(len(repr(repr(chr(int())))))
10,min(str(credits))
11,chr(len(str(range(int()))))
12,chr(len(set(str(type(bytes())))))
13,chr(len(str(type(int()))))
14,chr(len(str(type(not()))))
15,chr(len(str(type(float()))))
16,chr(len(str(type(object()))))
17,chr(len(str(type(complex()))))
18,chr(len(str(type(reversed(str())))))
19,chr(len(repr(str(type(complex())))))
20,chr(len(str(set(str(not())))))
21,chr(len(str(set(str(not()))))+int(not()))
22,chr(len(str(type(iter(set())))))
23,chr(len(str(type(iter(set()))))+int(not()))
24,chr(len(str(type(iter(bytes())))))
25,chr(len(str(set(str(set())))))
26,chr(len(str(type(iter(dict())))))
27,chr(len(str(type(iter(dict()))))+int(not()))
28,chr(len(str(type(iter(str())))))
29,chr(max(range(len(str(zip())))))
30,chr(len(str(zip())))
31,chr(len(str(zip()))+int(not()))
32,min(str(range(int())))
33,chr(ord(min(str(range(not()))))+int(not()))
34,min(repr(repr(str())))
35,chr(len(str(reversed(str()))))
36,chr(len(str(reversed(str())))+int(not()))
37,chr(len(str(reversed(str())))+len(str(dict())))
38,chr(len(str(reversed(str())))+len(hex(int())))
39,max(repr(str()))
40,min(str(set()))
41,max(str(tuple()))
42,chr(ord(max(str(tuple())))+int(not()))
43,chr(ord(max(str(tuple())))+len(str(dict())))
44,max(str(tuple(repr(str()))))
45,chr(sum(range(int(str(int(not()))+str(int())))))
46,min(str(float()))
47,chr(max(range(ord(str(int())))))
48,str(int())
49,str(int(not()))
50,str(len(str(dict())))
51,str(len(hex(int())))
52,str(len(str(not())))
53,str(len(str(set())))
54,str(len(str(complex(not()))))
55,max(str(ord(max(str(not())))))
56,max(str(ord(str(int()))))
57,max(str(ord(str(int(not())))))
58,chr(ord(str(int()))+ord(min(str(credits))))
59,chr(ord(str(int()))+len(str(range(int()))))
60,next(iter(str(object())))
61,chr(ord(str(int()))+len(str(type(int()))))
62,next(reversed(str(object())))
63,chr(ord(str(int()))+len(str(type(float()))))
64,chr(ord(str(int()))+len(str(type(object()))))
65,chr(ord(str(int()))+len(str(type(complex()))))
66,chr(sum(range(len(set(str(type(bytes())))))))
67,next(iter(str(copyright)))
68,chr(ord(next(iter(str(copyright))))+int(not()))
69,chr(ord(max(repr(str())))+len(str(zip())))
70,min(str(not(not())))
71,chr(ord(next(iter(str(not(not())))))+int(not()))
72,chr(ord(min(str(not(not()))))+len(str(dict())))
73,chr(ord(str(int()))+len(str(set(str(set())))))
74,chr(ord(str(int()))+len(str(type(iter(dict())))))
75,chr(ord(min(str(not(not()))))+len(str(set())))
76,chr(ord(str(int()))+len(str(type(iter(str())))))
77,chr(ord(str(int()))+max(range(len(str(zip())))))
78,chr(ord(str(int()))+len(str(zip())))
79,chr(ord(str(int()))+len(str(zip()))+int(not()))
80,chr(ord(min(str(set())))+ord(min(str(set()))))
81,chr(ord(max(str(tuple())))+ord(min(str(set()))))
82,chr(ord(str(int()))+ord(min(repr(repr(str())))))
83,chr(max(range(ord(min(str(not()))))))
84,min(str(not()))
85,chr(ord(min(str(not())))+int(not()))
86,chr(ord(min(str(not())))+len(str(dict())))
87,chr(ord(min(str(not())))+len(hex(int())))
88,chr(ord(min(str(not())))+len(str(not())))
89,chr(ord(min(str(not())))+len(str(set())))
90,chr(ord(min(str(not())))+len(str(complex(not()))))
91,chr(ord(min(str(not())))+len(repr(str(set()))))
92,max(repr(repr(repr(str()))))
93,chr(ord(max(repr(repr(repr(str())))))+int(not()))
94,chr(ord(str(int()))+ord(min(str(float()))))
95,min(max(vars()))
96,chr(ord(min(min(locals())))+int(not()))
97,chr(max(range(ord(max(bin(int()))))))
98,max(bin(int()))
99,chr(ord(max(bin(int())))+int(not()))
100,next(reversed(hex(ord(max(str(dict()))))))
101,next(reversed(str(not())))
102,next(iter(str(frozenset())))
103,chr(ord(next(iter(str(frozenset()))))+int(not()))
104,chr(ord(max(bin(int())))+len(str(complex(not()))))
105,chr(ord(max(bin(int())))+len(repr(str(set()))))
106,max(str(complex()))
107,chr(ord(max(str(complex())))+int(not()))
108,chr(ord(max(bin(int())))+ord(min(str(credits))))
109,chr(ord(max(bin(int())))+len(str(range(int()))))
110,chr(max(range(ord(max(oct(int()))))))
111,max(oct(int()))
112,chr(ord(max(oct(int())))+int(not()))
113,chr(ord(max(oct(int())))+len(str(dict())))
114,max(str(range(int())))
115,max(str(not(not())))
116,max(str(set()))
117,max(str(not()))
118,max(str(vars))
119,max(str(pow))
120,max(hex(int()))
121,max(str(credits))
122,max(str(zip))
123,min(str(dict()))
124,chr(ord(min(str(dict())))+int(not()))
125,max(str(dict()))
126,chr(ord(max(str(dict())))+int(not()))`;

const astrixData = `64,chr(ord(min(str(range(not()))))*(int(not())+int(not())))`;

const periodData = `66,max(str(bytes())).upper()
69,next(reversed(str(not()))).upper()
74,max(str(complex())).upper()
79,max(oct(int())).upper()
82,next(iter(str(range(not())))).upper()
83,max(str(not(not()))).upper()
85,max(str(not())).upper()
86,max(str(vars)).upper()
87,max(str(pow)).upper()
88,max(str(object())).upper()
89,max(str(credits)).upper()
90,max(str(zip)).upper()
91,chr(ord(max(str(zip)).upper())+int(not()))
99,next(iter(str(copyright))).lower()`;

const creditsData = `10,chr(len(str(set(bin(int())))))
58,chr(ord(str(int()))+len(str(set(bin(int())))))
108,chr(ord(max(bin(int())))+len(str(set(bin(int())))))
121,max(str(type(bytes())))`;

function mapCharacters(csvData) {
  const charMap = {};
  const rows = csvData.trim().split('\n');
  rows.slice(1).forEach(row => {
    const [char, func] = row.split(',');
    if (char && func) {
      charMap[char] = func;
    }
  });
  return charMap
}

const charMapPeriod = mapCharacters(periodData);
const charMapAstrix = mapCharacters(astrixData);
const charMapNoCredits = mapCharacters(creditsData);

function replaceAndJoin(input) {
  const asciiValues = Array.from(input, char => char.charCodeAt(0));
  let map = mapCharacters(csvData);
  if($('period').checked) Object.assign(map, charMapPeriod);
  if($('astrix').checked) Object.assign(map, charMapAstrix);
  if($('nocredits').checked) Object.assign(map, charMapNoCredits)
  let out = asciiValues.map(char => map[char] || `  <COULDNT FIND ${char}>  `).join('+');
  return $('eval').checked ? `exec(${out})` : out;
}
