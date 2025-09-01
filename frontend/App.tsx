// Default page for user prompt
import React from 'react';
import Input from './Input';

function App() {
  return (
    <div className="h-screen relative bg-gray-100 items-center justify-center">
      <div className="bg-white p-10 rounded-2xl text-center max-w-md w-full">
        <h1 className="text-3xl font-bold text-blue-600 text-center">
          What job are you looking for?
        </h1>
        <Input />
      </div>
    </div>
  );
}

export default App;
