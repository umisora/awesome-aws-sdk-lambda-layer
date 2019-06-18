awesome-aws-sdk-lambda-layer
====

Overview
Provides the latest AWS SDK Lambda Layer for use with AWS Lambda the latest AWS SDK Lambda Layer for use with AWS Lambda. 

## Description
I was creating a lightweight Lambda Code using only the AWS SDK with AWS Lambda, but it was unfortunate that there were Region and Service versions that were out of date. Besides Python and Node, there was no SDK, so it had to be packaged and deployed by itself.
I developed this because it was very inconvenient to package and push Lambda when deploying with GitOps using Terraform Enterprise.
Simply specify Arn in the Lambda Layer of the SDK provided in `awesome-aws-sdk-lambda-layer` as the Lambda Layer in Terraform, and a lightweight Lambda Code can be provided in Terraform.

私は AWS LambdaでAWS SDKだけを使用した軽量なLambda Codeを作成していたが、Versionが古くて使えないRegionやServiceがあって残念だった。またPythonやNode以外ではSDKすら入っておらず自らパッケージしてデプロイする必要があった。
私はTerraform Enterpriseを利用してGitOpsでデプロイする時にLambdaをPackagingしてPushするのが非常に不便だったのでこれを開発した。
TerraformでLambda Layerとして `awesome-aws-sdk-lambda-layer` で提供される SDKのLambda LayerのArnを指定するだけで軽量な Lambda CodeはTerraformで提供できる様になる。

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

