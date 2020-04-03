"use strict";

const AthenaExpress = require("athena-express"),
  aws = require("aws-sdk"),
  awsCredentials = {
    region: "us-east-1",
    accessKeyId: "AKIAIHV5B6DGMEXVCXGA",
    secretAccessKey: "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"
  };

aws.config.update(awsCredentials);

const athenaExpressConfig = {
  aws,
  s3: "s3://my-bucket-for-storing-athena-results-us-east-1",
    getStats: true
};

const athenaExpress = new AthenaExpress(athenaExpressConfig);

//Invoking a query on Amazon Athena
(async () => {
  let query = {
    sql: "SELECT elb_name, request_port, request_ip FROM elb_logs LIMIT 3",
    db: "sampledb",
    getStats: true 
  };

  try {
    let results = await athenaExpress.query(query);
    console.log(results);
  } catch (error) {
    console.log(error);
  }
})();