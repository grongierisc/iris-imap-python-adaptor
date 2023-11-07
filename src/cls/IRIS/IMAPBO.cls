Class IRIS.IMAPBO Extends Grongier.PEX.BusinessOperation [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter ADAPTER;

Parameter SETTINGS = "%classname:Python ,%module:Python ,%settings:Python ,%classpaths:Python ";

Property %classname As %String [ InitialExpression = "IMAPBO", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "");

Property %module As %String [ InitialExpression = "bo", Internal ];

}
