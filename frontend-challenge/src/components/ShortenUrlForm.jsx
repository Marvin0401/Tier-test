/* eslint no-unused-vars: 1 */

import React, { useCallback, useState } from 'react';

const ShortenUrlForm = () => {
    const [value, setValue] = useState('');
    const [result, setResult] = useState('');
    const [error, setError] = useState('');

    const onChange = useCallback(
        (e) => {
            // TODO: Set the component's new state based on the user's input
            setValue(e.target.value);
        },
        [
            /* TODO: Add necessary deps */
            value
        ],
    );

    const onSubmit = useCallback(
        (e) => {
            e.preventDefault();
            // TODO: shorten url and copy to clipboard
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ link: value })
            };
            fetch('http://localhost:8000/api/create', requestOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        navigator.clipboard.writeText(data.result);
                        setResult(data.result);
                        setError('');
                    }
                    else{
                        setError(data.error);
                        setResult('');
                    }
                });

        },
        [
            /* TODO: necessary deps */
            value
        ],
    );

    return (
        <form onSubmit={onSubmit}>
            <label htmlFor="shorten">
                Url:
                <input
                    placeholder="Url to shorten"
                    id="shorten"
                    type="text"
                    value={value}
                    onChange={onChange}
                />
            </label>
            <input type="submit" value="Shorten and copy URL" />
            {/* TODO: show below only when the url has been shortened and copied */}
            <div>{result}</div>
            <div style={{ color: 'red' }}>{error}</div>
        </form>
    );
};

export default ShortenUrlForm;
