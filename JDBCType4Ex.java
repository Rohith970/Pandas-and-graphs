import java.sql.*;

public class JDBCType4Ex
{
public static void main(String s[])throws Exception
{
String driverclass="oracle.jdbc.driver.OracleDriver";

String url="jdbc:oracle:thin:@192.168.63.144:1521:orcl";

String user="B2016";
String pass="aries3912";

Class.forName(driverclass);

System.out.println("driver loaded....");

Connection con=DriverManager.getConnection(url,user,pass);

System.out.println("connected");

Statement st=con.createStatement();

int count=st.executeUpdate("insert into patient values(100,'amith',9874563218,'02-12-08','tuberculosis')");

System.out.println(count);

}//main
}//class
