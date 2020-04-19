import styled from "styled-components";

export const Container = styled.div`

#app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 30px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

#app main {
  margin-left: 30px;
}

@media (max-width: 1000px) {
  #app {
    flex-direction: column;
  }

  #app main {
    margin-left: 0;
    margin-top: 10px;
  }
}

main {
  flex: 1;
}

main ul {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  list-style: none;
}

@media (max-width: 650px) {
  main ul {
    grid-template-columns: 1fr;
  }
}
#search {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px 30px;
  width: 100%;
  display: flex;
}
#search input {
  width: 100%;
  height: 50px;
  font-size: 14px;
  color: #666;
  border: 0;
  border-bottom: 1px solid #eee;
  padding-left: 20px;
}

#search button {
  width: 20%;
  height: 50px;
  font-size: 14px;
  background: #4285f4;
  color:#fff;
  border: 0;
  border-bottom: 1px solid #eee;
}
li.dash-item {
  background: #FFF;
  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.02);
  border-radius: 2px;
  padding: 20px;
}

li.dash-item header {
  display: flex;
  flex-direction: row;
  align-items: center;
}

li.dash-item header img {
  width: 80px;
  height: 80px;
  border-radius: 5%;
}

li.dash-item header .user-info {
  margin-left: 20px;
}

.user-info strong {
  display: block;
  font-size: 20px;
  color: #333;
}

.user-info span {
  font-size: 13px;
  color: #999;
  margin-top: 10px;
}

li.dash-item p {
  color: #666;
  font-size: 14px;
  line-height: 20px;
  margin: 10px 0;
}

li.dash-item a {
  color: #8e4dff;
  font-size: 14px;
  text-decoration: none;
}

li.dash-item a:hover {
  color: #5a2ea6;
}

`;