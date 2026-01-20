import "./App.css";
import { useEffect, useState } from "react";

function App() {
    const [caption, setCaption] = useState("");
    const [translation, setTranslation] = useState("");

    useEffect(() => {
        const interval = setInterval(async () => {
            const res = await fetch("http://localhost:8000/caption");
            const data = await res.json();
            setCaption(data.original);
            setTranslation(data.translated);
            console.log("Caption:", data.original);
        }, 300);

        return () => clearInterval(interval);
    }, []);

    return <div 
            style={{ fontSize: "2rem", padding: "40px" }}>
                {caption}
                {translation && <div style={{ marginTop: "20px", color: "gray" }}>
                    {translation}
                </div>}
           </div>;
}

export default App;
