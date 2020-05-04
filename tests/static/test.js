/*! This has to be more than 200 characters; otherwise it won't be compressed.
    This counts for the minified version too. Any file under 200 characters
    won't be compressed.
*/
'use strict';
(function ()
{
    function test_a()
    {
        var some_variable = 'value';
        let some_other_variable = 'value';
        return some_variable;
    }

    function test_b()
    {
        var some_variable = 'value';
        let some_other_variable = 'value';
        return some_variable;
    }

    function test_c()
    {
        var some_variable = 'value';
        let some_other_variable = 'value';
        return some_variable;
    }
})();
