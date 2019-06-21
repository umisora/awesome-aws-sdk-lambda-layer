awesome-aws-sdk-lambda-layer
====

Overview
Provides the latest AWS SDK Lambda Layer for use with AWS Lambda. 

AWS Lambdaで使用する最新のAWS SDK Lambda Layerを提供します。

## Description
I was creating a lightweight Lambda Code using only the AWS SDK with AWS Lambda, but it was unfortunate that there were Region and Service versions that were out of date. Besides Python and Node, there was no SDK, so it had to be packaged and deployed by itself.

I developed this because it was very inconvenient to package and push Lambda when deploying with GitOps using Terraform Enterprise.

Simply specify Arn in the Lambda Layer of the SDK provided in `awesome-aws-sdk-lambda-layer` as the Lambda Layer in Terraform, and a lightweight Lambda Code can be provided in Terraform.

私は aws lambdaでaws sdkだけを使用した軽量なlambda codeを作成していたが、versionが古くて使えないregionやserviceがあって残念だった。またpythonやnode以外ではsdkすら入っておらず自らパッケージしてデプロイする必要があった。

私はterraform enterpriseを利用してgitopsでデプロイする時にlambdaをpackagingしてpushするのが非常に不便だったのでこれを開発した。

terraformでlambda layerとして `awesome-aws-sdk-lambda-layer` で提供される sdkのlambda layerのarnを指定するだけで軽量な lambda codeはterraformで提供できる様になる。

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

