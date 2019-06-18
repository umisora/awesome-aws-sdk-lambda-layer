awesome-aws-sdk-lambda-layer
====

Overview
Provides the latest AWS SDK Lambda Layer for use with AWS Lambda the latest AWS SDK Lambda Layer for use with AWS Lambda. 

## Description
I was creating a lightweight Lambda Code using only the AWS SDK with AWS Lambda, but it was unfortunate that there were Region and Service versions that were out of date. Besides Python and Node, there was no SDK, so it had to be packaged and deployed by itself.
I developed this because it was very inconvenient to package and push Lambda when deploying with GitOps using Terraform Enterprise.
Simply specify Arn in the Lambda Layer of the SDK provided in `awesome-aws-sdk-lambda-layer` as the Lambda Layer in Terraform, and a lightweight Lambda Code can be provided in Terraform.

$B;d$O(B AWS Lambda$B$G(BAWS SDK$B$@$1$r;HMQ$7$?7ZNL$J(BLambda Code$B$r:n@.$7$F$$$?$,!"(BVersion$B$,8E$/$F;H$($J$$(BRegion$B$d(BService$B$,$"$C$F;DG0$@$C$?!#$^$?(BPython$B$d(BNode$B0J30$G$O(BSDK$B$9$iF~$C$F$*$i$:<+$i%Q%C%1!<%8$7$F%G%W%m%$$9$kI,MW$,$"$C$?!#(B
$B;d$O(BTerraform Enterprise$B$rMxMQ$7$F(BGitOps$B$G%G%W%m%$$9$k;~$K(BLambda$B$r(BPackaging$B$7$F(BPush$B$9$k$N$,Hs>o$KITJX$@$C$?$N$G$3$l$r3+H/$7$?!#(B
Terraform$B$G(BLambda Layer$B$H$7$F(B `awesome-aws-sdk-lambda-layer` $B$GDs6!$5$l$k(B SDK$B$N(BLambda Layer$B$N(BArn$B$r;XDj$9$k$@$1$G7ZNL$J(B Lambda Code$B$O(BTerraform$B$GDs6!$G$-$kMM$K$J$k!#(B

## Lambda Layer Arn

TBD:

## Requirement
TBD:

## Usage
TBD:

## Install
TBD:

## Contribution
TBD:

