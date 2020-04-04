"use strict";

const AthenaExpress = require("athena-express"),
  aws = require("aws-sdk"),
  awsCredentials = {
    region: "eu-north-1",
    accessKeyId: "---",
    secretAccessKey: "------"
  };

aws.config.update(awsCredentials);

const athenaExpressConfig = {
  aws,
  s3: "s3://covid-datasets/",
    getStats: true
};

const athenaExpress = new AthenaExpress(athenaExpressConfig);

const fastcsv = require('fast-csv');
const fs = require('fs');
const fsExtra = require('fs-extra')

fsExtra.emptyDirSync("./query-results/")



async function query_athena(queryStr, stateName) {
  let query = {
    sql: queryStr,
    db: "covid19",
    getStats: true 
  };

  try {
    let results = await athenaExpress.query(query);
    console.log(results.QueryExecutionId);
    console.log(results.S3Location);
    let ws = fs.createWriteStream("query-results/"+stateName+".csv");
    fastcsv
      .write(results.Items, { headers: true })
      .pipe(ws);

  } catch (error) {
    console.log(error);
  }
}
//Invoking a query on Amazon Athena
(async () => {
  
  let rawstates = fs.readFileSync('sql_timeseries_states.json');
  let statesObj = JSON.parse(rawstates);
  let states = statesObj.states;
  console.log(states);
  
    for (var i = 0; i < states.length; i++) {
      console.log(states[i].name, "   => qurey")
      query_athena(states[i].query, i+"_"+states[i].name)
    }
})();