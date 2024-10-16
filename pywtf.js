function $(id) {
  return document.getElementById(id);
}

// csv data loading
async function loadCSV(filename) {
  try {
    const response = await fetch(`data/${filename}.csv`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.text();
  } catch (error) {
    console.error(`Error loading ${filename}.csv:`, error);
    return '';
  }
}

// character mapping
function mapCharacters(csvData) {
  const charMap = {};
  const rows = csvData.trim().split('\n');
  rows.forEach(row => {
    const [char, func] = row.split(',');
    if (char && func) {
      charMap[char] = func;
    }
  });
  return charMap;
}

// global vars
let originalMappings, periodMappings, astrixMappings, newerPythonMappings;
let dataLoaded = false;

// load all csv data
async function loadAllData() {
  originalMappings = await loadCSV('originalMappings');
  periodMappings = await loadCSV('periodMappings');
  astrixMappings = await loadCSV('astrixMappings');
  newerPythonMappings = await loadCSV('newerPythonMappings');
  dataLoaded = true;
}

// initialise the loading of all the data
replaceAndJoin($('input').value)
            .then(output => {}).catch(error=>{});

async function replaceAndJoin(input) {
  // ensure all data is loaded
  if (!dataLoaded) {
    await loadAllData();
  }

  const asciiValues = Array.from(input, char => char.charCodeAt(0));
  let map = mapCharacters(originalMappings);

  if ($('period').checked) {
    const periodMap = mapCharacters(periodMappings);
    Object.assign(map, periodMap);
  }

  if ($('astrix').checked) {
    const astrixMap = mapCharacters(astrixMappings);
    Object.assign(map, astrixMap);
  }

  if ($('newerPython').checked) {
    const newerPythonMap = mapCharacters(newerPythonMappings);
    Object.assign(map, newerPythonMap);
  }

  let out = asciiValues.map(char => map[char] || `  <COULDNT FIND ${char}>  `).join('+');
  return $('eval').checked ? `exec(${out})` : out;
}
