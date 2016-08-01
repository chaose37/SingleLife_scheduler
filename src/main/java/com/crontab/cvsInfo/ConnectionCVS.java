package com.crontab.cvsInfo;

import java.io.DataOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import com.crontab.util.ConnectionPool;


public class ConnectionCVS {
	
	public static void deleteCVS() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_cvsInfo";
			
			pstmt = con.prepareStatement(sql);
			
			pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(pstmt != null) {
				pstmt.close();
			}
			if (con != null) {
				con.close();
			}
		}
	}
	
	public static void cuInfo() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//cu.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void sevenInfo() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//711.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

	public static void insertGS() throws Exception {
		URL url = new URL("http://gs25.gsretail.com/gscvs/ko/products/event-goods");
		URLConnection conn = url.openConnection();
		String jsessionIDStr = conn.getHeaderField("Set-Cookie");
		String sessionID = jsessionIDStr.split(";")[0].split("=")[1] + ";";
		String csrfToken = null;

		Scanner scanner = new Scanner(conn.getInputStream());

		while (true) {
			// <form id="CSRFForm"
			try {
				String line = scanner.nextLine();

				if (line.startsWith("<form id=\"CSRFForm\"")) {
					int idx = line.lastIndexOf("value=");
					String temp = line.substring(idx + 7);
					csrfToken = temp.substring(0, temp.length() - 4);
					break;
				}
			} catch (Exception e) {
				break;
			}
		}
		Connection con = null;
		PreparedStatement pstmt = null;

		HttpURLConnection connection = null;
		String targetURL = "http://gs25.gsretail.com/gscvs/ko/products/event-goods-search?CSRFToken=" + csrfToken;
		String postParams = "pageNum=1&pageSize=1000&searchType=&searchWord=&parameterList=TOTAL";

		try {
			// Create connection
			url = new URL(targetURL);
			connection = (HttpURLConnection) url.openConnection();
			connection.setRequestProperty("Cookie", "JSESSIONID=" + sessionID);
			connection.setRequestProperty("Accept-Language", "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4");
			connection.setRequestProperty("Accept", "application/json, text/javascript, */*; q=0.01");
			connection.setUseCaches(false);
			connection.setDoInput(true);
			connection.setDoOutput(true);

			// Send request
			DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
			wr.writeBytes(postParams);
			wr.flush();
			wr.close();

			// Get Response
			InputStream is = connection.getInputStream();
			Scanner sc = new Scanner(is, "UTF-8");
			String line = sc.nextLine();

			line = line.replaceAll("\\\\", "");

			line = line.substring(1, line.length() - 1);

			JSONParser jsonParser = new JSONParser();
			JSONObject jsonObject = (JSONObject) jsonParser.parse(line);
			JSONArray resultInfoArray = (JSONArray) jsonObject.get("results");

			con = ConnectionPool.getConnection();

			String sql = "insert into sl_cvsInfo(prodName, price, event , image, store, giftName, giftImage) "
					   + "values (?, ?, ?, ?, ?, ?, ?)";
			for (int i = 0; i < resultInfoArray.size(); i++) {

				// 배열 안에 있는것도 JSON 형식 이기 때문에 JSON Object 로 추출
				JSONObject resultObject = (JSONObject) resultInfoArray.get(i);
				String price = Double.toString((Double) resultObject.get("price"));
				int index = price.indexOf(".");
				price = price.substring(0, index);

//				// JSON name 으로 추출
//				System.out.println("resultInfo : store --> GS");
//				System.out.println("resultInfo : goodsName --> " + resultObject.get("goodsNm"));
//				System.out.println("resultInfo : price --> " + price);
//				System.out.println("resultInfo : attFileNm --> " + resultObject.get("attFileNm"));
//				System.out.println("resultInfo : giftGoodsNm --> " + resultObject.get("giftGoodsNm"));
//				System.out.println("resultInfo : giftAttFileNm --> " + resultObject.get("giftAttFileNm"));
//				System.out.println("resultInfo : eventTypeNm --> " + resultObject.get("eventTypeNm"));

				pstmt = con.prepareStatement(sql);

				pstmt.setString(1, (String) resultObject.get("goodsNm"));
				pstmt.setString(2, price);
				pstmt.setString(3, (String) resultObject.get("eventTypeNm"));
				pstmt.setString(4, (String) resultObject.get("attFileNm"));
				pstmt.setString(5, "GS");
				pstmt.setString(6, (String) resultObject.get("giftGoodsNm"));
				pstmt.setString(7, (String) resultObject.get("giftAttFileNm"));

				pstmt.executeUpdate();
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (connection != null) {
				connection.disconnect();
			}
			if (pstmt != null) {
				try {
					pstmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			ConnectionPool.release(con);
		}
	}
}