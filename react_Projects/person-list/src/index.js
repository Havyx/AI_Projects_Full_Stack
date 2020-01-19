import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";

ReactDOM.render(<App />, document.getElementById("root"));

const Person = ({ img, name, job, children }) => {
  console.log(Person);
  const url = `https://randomuser.me/api/portraits/thumb/men/${img}.jpg`;
  return (
    <article className="person">
      <img src={url} alt="Person"></img>
      <h4>{name}</h4>
      <h4>{job}</h4>
      <p>{children}</p>
    </article>
  );
};

const PersonList = () => {
  return (
    <section className="person-list">
      <Person img="33" name="Jane" job="Developer" />
      <Person img="34" name="June" job="Designer">
        <p>
          Demonstração de como passar objetos filhos pelo componente (Isso é um
          objeto filho)
        </p>
      </Person>
      <Person img="35" name="jonh" job="Tester" />
      <Person img="36" name="josh" job="Scrum Master" />
    </section>
  );
};

ReactDOM.render(<PersonList />, document.getElementById("person-l"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
