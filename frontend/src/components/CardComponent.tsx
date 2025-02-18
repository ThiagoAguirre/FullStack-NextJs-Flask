import React from 'react';

interface Card{
    id: number;
    name: string;
    email: string;
}

const CardComponent: React.FC<Card> = ({id, name, email}) => {
    return (
        <div className="card">
            <h2>{name}</h2>
            <p>{email}</p>
        </div>
    );
}
